from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import pydantic

def generate_image(prompt, filename="images/temp.png", model="gemini-2.0-flash-preview-image-generation"):
    """
    Generate an image using Google's Gemini API
    
    Args:
        prompt (str): Text description of the image to generate
        filename (str): Path where the image should be saved
        model (str): Gemini model to use for generation
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        client = genai.Client()
        
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=['TEXT', 'IMAGE']
            )
        )
        
        # Look for image data in the response
        for part in response.candidates[0].content.parts:
            if part.text is not None:
                print(f"Gemini response: {part.text}")
            elif part.inline_data is not None:
                # Convert the inline data to a PIL image and save
                image = Image.open(BytesIO(part.inline_data.data))
                image.save(filename)
                print(f"Image saved to: {filename}")
                return True
        
        print("No image data found in response")
        return False
        
    except Exception as e:
        print(f"Error generating image: {e}")
        return False
