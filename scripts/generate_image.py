from openai import OpenAI
import base64

def generate_image(prompt, filename="images/temp.png", model="dall-e-2"):
    client = OpenAI()
    
    result = client.images.generate(
        model=model,
        prompt=prompt,
        response_format="b64_json"
    )
    
    image_base64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)
    
    # Save the image to a file
    with open(filename, "wb") as f:
        f.write(image_bytes)
    
    return True
