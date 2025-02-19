Te toca usar el .yml que hay aquí o una herramienta parecida, aquí se está usando debugpy para que se conecte al debugger de VSC.

Luego de correr el compose con ```docker compose -f docker-compose.yml -f docker-compose.debug.yml up```, dale a:

Run and Debug (ícono sidebar) > "create a launch .json file" > Python Debugger > Remote Attach > localmachine > <url y/o puerto> (5678 en nuestro caso)

Botón de run, y se nos abre una terminal  
Pon un punto rojo de stop en el código que quieres  
Y pruebas haciéndole una request a eso