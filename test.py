from service.ai_service import DeepLService, AIService

deepl_service = DeepLService()
ai_service = AIService()

size = {
    "small": "256x256",
    "medium": "512x512",
    "large": "1024x1024",
    "wide": "1792x1024",
    "tall": "1024x1792"
}

translate_content = deepl_service.translate({
                    "content": "만화 배경의 그래프 아이콘",
                    "target_lang": "EN-US"
                })
print(translate_content)

url = ai_service.handling_image({
                    "job": "GENERATE",
                    "content": translate_content,
                    "size": size['wide']
                })
print(url)

ai_service.download_image({
                    "url": url,
                    "image_name": "test.jpg"
                })