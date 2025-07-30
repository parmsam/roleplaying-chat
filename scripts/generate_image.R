library(reticulate)
library(ellmer)

source_python("scripts/generate_image.py")

generate_image2 <- function(prompt, filepath) {
  generate_image(prompt = prompt, filename = filepath)
  return(filepath)
}

register_generate_image_tool <- function(chat, ...) {
  rlang::check_installed("ellmer")
  
  chat$register_tool(
    ellmer::tool(
      generate_image2,
      "Generate image using DALL-E-2 and save in a file.",
      .description = "Given a prompt and file path, generates an image using DALL-E-2 and saves it to the specified file. You should only specify friendly sensible file names like otter.png or walrus.png. Ensure they are unique.",
      prompt = ellmer::type_string("The prompt to generate the image from."),
      filepath = ellmer::type_string(
        "Unique file path where the generated image will be saved. Name should be snakecase. You should always start the filepath with images/ to ensure it is placed in the images folder."
      )
    )
  )
  invisible(chat)
}

if (FALSE) {
  chat <- chat_openai()
  register_generate_image_tool(chat)
  chat$chat("Give me a golden dog with bad hair")
}
