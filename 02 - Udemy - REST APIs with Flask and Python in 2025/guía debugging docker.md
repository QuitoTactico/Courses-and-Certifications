Te toca usar el .yml que hay aquí o una herramienta parecida, aquí se está usando debugpy para que se conecte al debugger de VSC.

Luego de correr el compose de debug con ```docker compose -f docker-compose.yml -f docker-compose.debug.yml up```, dale a:

Run and Debug (ícono sidebar) > "create a launch .json file" > Python Debugger > Remote Attach > localhost > <url y/o puerto> (5678 en nuestro caso)

Botón de run verde a la izquierda, y se nos abre una terminal. Pon un punto rojo de stop en el código que quieres, y pruebas haciéndole una request a eso.

El código se va a parar en ese punto, y con la terminal podrás correr líneas antes de esa. Con la barra de herramientas puedes seguir la ejecución y ver cómo se crean variables.