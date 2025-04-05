from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

def generate_image(prompt, output_filename='generated_image.png'):
    # Load the pre-trained model (Stable Diffusion)
    pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4-original", 
                                                  torch_dtype=torch.float16)
    pipe.to("cuda")  # Use GPU if available (recommended for faster inference)
    
    # Generate the image based on the given prompt
    image = pipe(prompt).images[0]
    
    # Save the generated image
    image.save(output_filename)
    print(f"Image saved as {output_filename}")
    return image

if __name__ == "__main__":
    # Example prompt
    prompt = "A futuristic city skyline with flying cars"
    generate_image(prompt)
import openai
from PIL import Image
import io

# Your OpenAI API key (make sure to replace with your actual API key)
openai.api_key = 'your-openai-api-key'

def generate_image_dalle(prompt):
    # Request image generation from DALL·E 2
    response = openai.Image.create(
        prompt=prompt,
        n=1,  # Number of images to generate
        size="1024x1024"  # Size of the generated image
    )

    # Retrieve the image URL
    image_url = response['data'][0]['url']

    # Download the image
    image_data = openai.Image.download(image_url)

    # Convert to image format
    image = Image.open(io.BytesIO(image_data))
    image.show()

    # Save the image to a file
    image.save('generated_image_dalle.png')
    print("Image saved as 'generated_image_dalle.png'")

if __name__ == "__main__":
    # Example prompt
    prompt = "A futuristic city skyline with flying cars"
    generate_image_dalle(prompt)
