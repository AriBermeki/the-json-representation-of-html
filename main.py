import ui






layout = ui.Div(content=[
    ui.A(content='Home'),
    ui.A(content='Dashboard'),
    ui.A(content='Users', style={
      "margin": "120px"
    })
], style={
      "color": "red",
      "font-size": "16px",
      "padding":"10px",
      "margin": "120px"
    },)





if __name__ == '__main__':
    app = ui.UI(layout=layout)
    app.run()
