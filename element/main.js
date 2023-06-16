

// Beispiel-Element mit Events
const exampleElement = {
    id: 1,
    events: [
      {
        type: 'click',
        specials: ['one', 'two'],
        args: ['1', '2'],
        throttle: 100,
        leading_events: true,
        trailing_events: false,
        listener_id: 123
      },
      {
        type: 'mouseover',
        specials: ['three', 'four'],
        args: ['eventArg3', 'eventArg4'],
        throttle: 200,
        leading_events: false,
        trailing_events: true,
        listener_id: 456
      }
    ]
  };
  
  // Funktion zur Verarbeitung der Element-Events
  function processElementEvents(element) {
    element.events.forEach((event) => {
      let event_name = 'on' + event.type[0].toLocaleUpperCase() + event.type.substring(1);


      
      event.specials.forEach(s => event_name += s[0].toLocaleUpperCase() + s.substring(1));
      let handler = (e) => {
        const all = (typeof e !== 'object' || e === null) || !event.args;
        const args = all ? e : Object.fromEntries(event.args.map(a => [a, e[a]]));
  
        console.log('Event:', event_name);
        console.log('Arguments:', args);
      };
  
      // Hier könnten weitere Aktionen mit dem Event-Handler und den Event-Daten durchgeführt werden
  
      // Beispiel: Event-Listener hinzufügen
      document.addEventListener(event_name, handler);
    });
  }
  
  // Aufruf der Funktion mit dem Beispiel-Element
  processElementEvents(exampleElement);