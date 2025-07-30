library(ellmer)
library(shiny)
library(shinychat)
library(bslib)

source("scripts/utilities.R")
source("scripts/generate_image.R")

welcome_message <- ellmer::interpolate_file(
  "welcome-message.md"
)

additional_info <- ellmer::interpolate_file(
  "additional-info.md"
)

system_prompt <- ellmer::interpolate_file(
  "system-prompt.md",
  welcome_message = welcome_message,
  additional_info = additional_info
)

addResourcePath("images", "images")

ui <- bslib::page_sidebar(
  tags$style(HTML("
    img {
      width: 300px !important;
      height: auto;
    }
  ")),
  tags$div(
    style = "display: flex; align-items: center; justify-content: space-between; width: 100%; position: relative; z-index: 1000; margin-bottom: 0.25rem;",
    tags$h4("Roleplaying Chat", style = "margin: 0;"),
    actionButton(
      "open_settings",
      label = NULL,
      icon = shiny::icon("gear"),
      class = "btn-default",
      style = "margin-left: auto; padding: 0.2rem 0.4rem; font-size: 1.1rem; height: 2rem; width: 2rem; min-width: 2rem; border: none; background: transparent; color: #495057; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: none;",
    )
  ),
  sidebar = bslib::sidebar(
    markdown("Paws & Perils: Sadie's Big World Adventure"),
    tags$a(
      class = "btn btn-outline-primary btn-sm",
      href = "https://github.com/parmsam/roleplaying-chat",
      target = "_blank",
      tags$i(class = "fa fa-github me-2"),
      "View on GitHub"
    ),
    class = "text-center"
  ),
  shinychat::chat_ui(
    "chat",
    messages = 
      list(
        welcome_message
      )
  )
)
server <- function(input, output, session) {
  chat <- ellmer::chat_openai(
    model = "gpt-4.1-nano",
    system_prompt = system_prompt,
    api_args = list(temperature = 0.2)
  )
  
  register_generate_image_tool(chat)
  
  observeEvent(input$chat_user_input, {
    stream <- chat$stream_async(input$chat_user_input)
    shinychat::chat_append("chat", stream)
  })
  
  observeEvent(input$open_settings, {
    showModal(
      modalDialog(
        title = "Settings",
        "Placeholder.",
        easyClose = TRUE
      )
    )
  })
  
}

shinyApp(ui, server)
