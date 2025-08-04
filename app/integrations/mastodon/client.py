from mastodon import Mastodon


def publish_message(
    *,
    message: str,
) -> str:
    """
    Публикует сообщение в Mastodon.

    Args:
        message (str): Сообщение для публикации

    Returns:
        str: URL опубликованного туита.
    """
    if not message or message.strip() == "":
        print("Сообщение не может быть пустым.")
        return

    mastodon = Mastodon(
        access_token="toot_usercred.secret",
        api_base_url="https://fosstodon.org",
    )

    try:
        status = mastodon.toot(message)
        return status["url"]
    except Exception as e:
        print(f"Ошибка при публикации: {e}")
