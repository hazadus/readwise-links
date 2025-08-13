from atproto import Client


def publish_message(
    *,
    message: str,
    identifier: str,
    password: str,
) -> str:
    """
    Публикует сообщение в Bluesky.

    Args:
        message (str): Сообщение для публикации
        identifier (str): Идентификатор пользователя Bluesky
        password (str): Пароль пользователя Bluesky

    Returns:
        str: URL опубликованного skeet'а.
    """
    if not message or message.strip() == "":
        print("Сообщение не может быть пустым.")
        return ""

    if not identifier or not password:
        print("Идентификатор и пароль пользователя Bluesky обязательны.")
        return ""

    try:
        # Создаем клиент и авторизуемся
        client = Client()
        login_result = client.login(identifier, password)

        if not login_result:
            print("Ошибка авторизации в Bluesky")
            return ""

        print(f"Успешно авторизован как {identifier}")

        # Проверяем длину сообщения (Bluesky ограничивает 300 символами)
        if len(message) > 300:
            print(
                f"ВНИМАНИЕ: Сообщение длиной {len(message)} символов превышает лимит Bluesky (300)"
            )
            # Обрезаем сообщение до 300 символов
            message = message[:297] + "..."
            print(f"Сообщение обрезано до: {len(message)} символов")

        print(f"Публикуем в Bluesky: {repr(message)}")

        # Публикуем пост с использованием facets для лучшего распознавания ссылок
        try:
            # Создаем facets для ссылок и хештегов в тексте
            facets = []
            import re

            # Ищем URL в тексте - улучшенное регулярное выражение
            url_pattern = r"https?://[^\s\n]+"
            urls = re.findall(url_pattern, message)

            print(f"Найдено URL в сообщении: {urls}")

            for url in urls:
                # Находим позицию URL в тексте
                start_char = message.find(url)
                end_char = start_char + len(url)

                # Конвертируем позиции символов в байты для UTF-8
                start_bytes = len(message[:start_char].encode("utf-8"))
                end_bytes = len(message[:end_char].encode("utf-8"))

                print(f"URL: {url}")
                print(f"  Позиция символов: {start_char}-{end_char}")
                print(f"  Позиция байтов: {start_bytes}-{end_bytes}")

                facets.append(
                    {
                        "index": {"byteStart": start_bytes, "byteEnd": end_bytes},
                        "features": [
                            {"$type": "app.bsky.richtext.facet#link", "uri": url}
                        ],
                    }
                )

            # Ищем хештеги в тексте
            hashtag_pattern = r"#[a-zA-Zа-яё0-9_]+"
            hashtags = re.findall(hashtag_pattern, message)

            print(f"Найдено хештегов в сообщении: {hashtags}")

            for hashtag in hashtags:
                # Находим позицию хештега в тексте
                start_char = message.find(hashtag)
                end_char = start_char + len(hashtag)

                # Конвертируем позиции символов в байты для UTF-8
                start_bytes = len(message[:start_char].encode("utf-8"))
                end_bytes = len(message[:end_char].encode("utf-8"))

                print(f"Хештег: {hashtag}")
                print(f"  Позиция символов: {start_char}-{end_char}")
                print(f"  Позиция байтов: {start_bytes}-{end_bytes}")

                facets.append(
                    {
                        "index": {"byteStart": start_bytes, "byteEnd": end_bytes},
                        "features": [
                            {
                                "$type": "app.bsky.richtext.facet#tag",
                                "tag": hashtag[1:],
                            }  # Убираем # из тега
                        ],
                    }
                )

            if facets:
                print(f"Добавляем {len(facets)} facets (ссылки + хештеги):")
                for i, facet in enumerate(facets):
                    facet_type = "ссылка" if "link" in str(facet) else "хештег"
                    print(f"  Facet {i+1} ({facet_type}): {facet}")
                post = client.send_post(text=message, facets=facets)
            else:
                print("Facets не найдены, публикуем без них")
                post = client.send_post(text=message)

        except Exception as e:
            print(f"Ошибка при публикации с facets: {e}")
            # Fallback к обычной публикации
            post = client.send_post(text=message)

        # Формируем URL поста
        post_url = (
            f"https://bsky.app/profile/{identifier}/post/{post.uri.split('/')[-1]}"
        )

        print(f"Пост успешно опубликован:")
        print(f"URI: {post.uri}")
        print(f"CID: {post.cid}")
        print(f"URL: {post_url}")

        return post_url

    except Exception as e:
        print(f"Ошибка при публикации в Bluesky: {e}")
        return ""
