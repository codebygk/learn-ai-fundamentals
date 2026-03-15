from brochurizer import Brochurizer
from helpers.url_helper import is_url_reachable, is_url_valid, normalize_url


def prompt_for_url():
    while True:
        url = input("Enter the URL of the page to create brochure: ").strip().lower()
        url = normalize_url(url)
        if not is_url_valid(url):
            continue
        if not is_url_reachable(url):
            continue
        print(f"Selected URL: {url}")
        return url

def prompt_for_translation():
    while True:
        supported_languages = ["spanish", "english", "french", "chinese", "german"]
        language = input(f"Enter the language to translate the brochure. (Default: None. "
                         f"Supported: {supported_languages}): ").strip().lower()
        if not language:
            print(f"Translation language was not specified. Brochure will not be translated.")
            return None
        if language not in supported_languages:
            print(f"Translation language was not supported. "
                  f"Please select a valid language from {supported_languages}.")
            continue
        print(f"Selected Language: {language}")
        return language


def prompt_for_export():
    export = input("Do you want to export the brochure as a markdown file? (Y/n): ").strip().lower() or 'y'
    return export == 'y'



def main():
    while True:
        try:
            url = prompt_for_url()
            language = prompt_for_translation()
            export = prompt_for_export()
            brochurizer = Brochurizer(url=url)
            brochurizer.create_brochure(language=language, export=export)
            break
        except (ValueError, OSError) as e:
            print(f"Brochure creation failed: {e}")
            retry = input("Do you want to retry? (Y/n): ").strip().lower() or 'y'
            if retry != 'y':
                break
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break


if __name__ == '__main__':
    main()
