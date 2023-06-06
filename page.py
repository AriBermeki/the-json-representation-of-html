from inspect import signature 

class Page:
    def __init__(self, url='', name='', builder='', auth_needed=None, description=''):
        self.name = name
        self.url = url
        self.auth_needed = auth_needed
        self.builder = builder
    
    def as_list(self, param='', all_params=None):
        def call_builder():
            num_func_params = len(signature(self.builder).parameters)
            if num_func_params > 1:
                return self.builder(param, all_params)
            elif num_func_params > 0:
                return self.builder(param)
            else:
                return self.builder()
        return {
            'name': self.name,
            'content': call_builder()
        }
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://unpkg.com/react@latest/umd/react.development.js" crossorigin="anonymous"></script>
    <script src="https://unpkg.com/react-dom@latest/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/babel-standalone@latest/babel.min.js" crossorigin="anonymous"></script>
     
    <!-- Ant Design Components and Icons -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/antd/4.18.5/antd.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/ant-design-icons/4.7.0/index.umd.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/antd/4.18.5/antd.min.css" />
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
      
    </script>
    <title>Document</title>
</head>
<body>
    <div id="root"></div>

    <script type="text/babel">
    
    
        function fetchDataFromURL(url) {
          fetch(url)
            .then(response => response.json())
            .then(data => {
              console.log("Daten erfolgreich heruntergeladen:");
              console.log(data);
              // Hier kannst du weitere Aktionen mit den heruntergeladenen Daten durchführen
            })
            .catch(error => {
              console.log("Fehler beim Herunterladen der Daten:");
              console.error(error);
            });
        }

        function DynamicComponent({json}) {
            

            const renderElement = (element) => {
                const { type, child, style, ...props } = element;

                if (type === 'img') {
                return <img {...props} />;
                }

                return React.createElement(type, { style, ...props }, child);
            };

            return (
                <div>
                {Object.values(json).map((element) => (
                    <React.Fragment key={element.event_handler}>
                    {renderElement(element)}
                    </React.Fragment>
                ))}
                </div>
            );
        }

        const pyload = {{ elements | safe }}
        const response = {
            'status_code': 200,
            'background': null,
            'body': pyload
        };
        response.body = response.body.slice(1, -1);
        const jsonObject = JSON.parse(response.body)
        ReactDOM.render(<DynamicComponent json={ jsonObject} />, document.querySelector('#root'));

    </script>
</body>
</html>





<!--

import React from 'react';

function DynamicComponent() {
  const json = {
    "220fa4fa-03f5-11ee-a340-3e1e058d64da": {
      "className": "container",
      "event_handler": "220fa4fa-03f5-11ee-a340-3e1e058d64da",
      "type": "div",
      "id": "my-div",
      "child": "Dies ist ein <div>-Element."
    },
    "220fa572-03f5-11ee-a340-3e1e058d64da": {
      "style": { color: "red" },
      "event_handler": "220fa572-03f5-11ee-a340-3e1e058d64da",
      "type": "span",
      "id": "my-span",
      "child": "Dies ist ein <span>-Element."
    },
    "220fa59a-03f5-11ee-a340-3e1e058d64da": {
      "event_handler": "220fa59a-03f5-11ee-a340-3e1e058d64da",
      "type": "h1",
      "id": "my-heading",
      "child": "Dies ist ein <h1>-Element."
    },
    "220fa5b8-03f5-11ee-a340-3e1e058d64da": {
      "align": "center",
      "event_handler": "220fa5b8-03f5-11ee-a340-3e1e058d64da",
      "type": "p",
      "id": "my-paragraph",
      "child": "Dies ist ein <p>-Element."
    },
    "220fa5fe-03f5-11ee-a340-3e1e058d64da": {
      "width": 200,
      "height": 150,
      "event_handler": "220fa5fe-03f5-11ee-a340-3e1e058d64da",
      "type": "img",
      "id": "my-image",
      "src": "image.jpg",
      "alt": "Ein Bild"
    },
    "220fa626-03f5-11ee-a340-3e1e058d64da": {
      "event_handler": "220fa626-03f5-11ee-a340-3e1e058d64da",
      "type": "a",
      "id": "my-link",
      "child": "Dies ist ein Link",
      "href": "https://www.example.com"
    }
  };

  const renderElement = (element) => {
    const { type, child, style, ...props } = element;

    if (type === 'img') {
      return <img {...props} />;
    }

    return React.createElement(type, { style, ...props }, child);
  };

  return (
    <div>
      {Object.values(json).map((element) => (
        <React.Fragment key={element.event_handler}>
          {renderElement(element)}
        </React.Fragment>
      ))}
    </div>
  );


