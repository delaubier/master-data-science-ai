#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    https://shiny.posit.co/
#

library(shiny)
library(colourpicker)

# Define UI for application that draws a histogram
fluidPage(

    # Application title
    titlePanel("Premiers pas avec shiny"),
  
    # Summary
    verbatimTextOutput("summary"),
    
    # Sidebar with a slider input for number of bins
    sidebarLayout(
        sidebarPanel(
            textInput(inputId = "idText", label = "Enter a text", value = "Test"),
            sliderInput("bins",
                        "Number of bins:",
                        min = 1,
                        max = 50,
                        value = 30),
            colourInput(inputId = "color", label = "Couleur :",
                        value= "red"),
            radioButtons(inputId = "idRadio", label = "Select one",
                         choices = colnames(faithful)),
            textOutput(outputId = "NbBins")
            ),

        # Show a plot of the generated distribution
        mainPanel(
            plotOutput("distPlot")
        )
    )
)
