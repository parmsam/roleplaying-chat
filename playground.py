# /// script
# [tool.marimo.runtime]
# auto_instantiate = false
# ///

import marimo

__generated_with = "0.14.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from google import genai
    from google.genai import types
    from PIL import Image
    from io import BytesIO
    import base64
    from dotenv import load_dotenv

    return BytesIO, Image, genai, types


@app.cell
def _(client, genai):
    client2 = genai.Client()

    response2 = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Explain how AI works in a few words",
    )

    print(response2.text)
    return


@app.cell
def _(BytesIO, Image, genai, types):
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

    return (generate_image,)


@app.cell
def _(generate_image):
    prompt = ("Hi, can you create a 3d rendered image of a dog "
              "with wings and a top hat flying over a happy "
              "futuristic scifi city with lots of greenery?")

    success = generate_image(prompt, "gemini_generated_image.png")
    if success:
        print("Image generation completed successfully!")
    else:
        print("Image generation failed.")
    return


if __name__ == "__main__":
    app.run()
