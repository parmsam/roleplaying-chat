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
    from openai import OpenAI
    import base64
    from dotenv import load_dotenv
    import os
    # Load environment variables from the .env file
    load_dotenv(".env")
    return OpenAI, base64


@app.cell
def _(OpenAI, base64):
    def generate_image(prompt, filename="otter.png", model="dall-e-2"):
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
    
    prompt = "Generate an image of gray tabby cat hugging an otter with an orange scarf"
    generate_image(prompt, filename = "otter.png", model = "dall-e-2")
    return


if __name__ == "__main__":
    app.run()
