library(shiny)
library(colourpicker)

# Define server logic required to draw a histogram
function(input, output, session) {
  
    output$summary <- renderPrint({
      summary(faithful)
    })

    output$distPlot <- renderPlot({

        # generate bins based on input$bins from ui.R
        x    <- faithful[, input$idRadio]
        bins <- seq(min(x), max(x), length.out = input$bins + 1)
        output$NbBins <- renderText(paste0("Nombre de classes : ", input$bins))

        # draw the histogram with the specified number of bins
        hist(x, breaks = bins, col = input$color, border = 'white',
             xlab = 'Waiting time to next eruption (in mins)',
             main = input$idText)

    })

}
