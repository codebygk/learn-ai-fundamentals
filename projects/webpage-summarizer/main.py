
from helpers.url_helper import is_url_reachable, is_url_valid, normalize_url
from summarizer import Summarizer

        
def prompt_for_url():
    while True:
        url = input("Enter the URL of the page to summarize: ").strip().lower()
        url = normalize_url(url)
        if not is_url_valid(url):
            continue
        if not is_url_reachable(url):
            continue
        print(f"Selected URL: {url}")
        return url


def main():
    while True:
        try:
            url = prompt_for_url()
            summarizer = Summarizer(url)
            summarizer.summarize()
            break
        except (ValueError, OSError) as e:
            print(f"Summarization failed: {e}")
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
