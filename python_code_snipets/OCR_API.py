import requests

def extract_text_from_image(image_path, api_key):
    url = 'https://api.ocr.space/parse/image'
    with open(image_path, 'rb') as f:
        response = requests.post(
            url,
            files={'filename': f},
            data={
                'apikey': api_key,
                'language': 'eng',
                'isOverlayRequired': False
            }
        )
    result = response.json()
    if result['IsErroredOnProcessing']:
        print("Error:", result['ErrorMessage'])
    else:
        parsed_text = result['ParsedResults'][0]['ParsedText']
        print("Extracted Text:\n", parsed_text)

# Example usage
extract_text_from_image("sample_image.png", "your_api_key_here")
