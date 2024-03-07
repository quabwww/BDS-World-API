api = "https://yysq5h-8080.csb.app"
function = {
    "addButton": {
        "name":
        "$addButton[]",
        "tag":
        "$addButton[Nueva fila;ID de botón/URL;Etiqueta;Estilo;(Disabled;Emoji;ID de mensaje)]",
        "description":
        "Agrega un botón a la respuesta simple o Inserción",
        "example": [
            "$nomention\nEjemplo de boton\n$addButton[false;ID-;Dame click;primary;false;]"
        ],
        "images_example": [
            f"{api}/funcion/images/addButton.png"],
        "deprecated": False,
    },
    "addCmdReactions": {
        "name":
        "$addCmdReactions[]",
        "tag":
        "$addCmdReactions[Emojis;..]",
        "description":
        "Agrega reacciones a los disparadores",
        "example": ["$nomention\n$addCmdReactions[$message]"],
        "images_example": [
            f"{api}/funcion/images/addCmdReactions.png"
        ],
        "deprecated":
        False
    },
    "addEmoji": {
        "name":
        "$addEmoji[]",
        "tag":
        "$addEmoji[Nombre;URL de la imagen;¿devolver emoji si/no?]",
        "description":
        "Agrega un emoji a un servidor",
        "example": [
            "$nomention\n$var[url;https://cdn.discordapp.com/emojis/1152410822203674664.png?v=1]\nNuevo Emoji agregado al servidor $addEmoji[BDS;$var[url];true]"
        ],
        "images_example": [
            f"{api}/funcion/images/addEmoji.png"
        ],
        "deprecated":
        False,
    },
    "addField": {
        "name":
        "$addField[]",
        "tag":
        "$addField[Nombre;Valor;(En línea?;Índice)]",
        "description":
        "Agrega un campo a una inserción, o mejor dicho, a un embed.",
        "example": [
            "$nomention\n$addField[¡Este es el nombre del campo! #1;¡Éste es el valor del campo! #1]\n$addField[¡Este es el nombre del campo! #2;¡Éste es el valor del campo! #2]\n$addField[¡Este es el nombre del campo! #3;¡Éste es el valor del campo! #3]",
            "$nomention\n$addField[¡Este es el nombre del campo! #1;¡Éste es el valor del campo! #1;true]\n$addField[¡Este es el nombre del campo! #2;¡Éste es el valor del campo! #2;true]\n$addField[¡Este es el nombre del campo! #3;¡Éste es el valor del campo! #3;true]"
        ],
        "images_example": [
            f"{api}/funcion/images/addField-1.png",
            f"{api}/funcion/images/addField-2.png"
        ],
        "deprecated":
        False,
    },
    "addMessageReactions": {
        "name":
        "$addMessageReactions[]",
        "tag":
        "$addMessageReactions[Canal ID;Mensaje ID;Emojis;..]",
        "description":
        "Agrega reacciones a un mensaje",
        "example": [
            "$nomention\n$addMessageReactions[$channelID;$message[1];$message[2]]"
        ],
        "images_example": [
            f"{api}/funcion/images/addMessageReactions.png"
        ],
        "deprecated":
        False,
    },
    "addReactions": {
        "name":
        "$addReactions[]",
        "tag":
        "$addReactions[emojis;...]",
        "description":
        "Agrega reacciones a la respuesta simple o inserción del bot.",
        "example":
        ["$nomention\nEmoji agregado al mensaje del bot.\n$addReactions[✅]"],
        "images_example": [
            f"{api}/funcion/images/addReactions.png"
        ],
        "deprecated":
        False,
    },
    "addSelectMenuOption": {
        "name":
        "$addSelectMenuOption[]",
        "tag":
        "$addSelectMenuOption[ID de opción de menú;etiqueta;valor;descripción;(¿predeterminado si/no?;emoji;ID de mensaje)]",
        "descripcion":
        "Agrega la opción de menú de selección a un menú de selección.",
        "example": [
            "$nomention\n$newSelectMenu[Ejemplo;1;1;Elija alguna opción]\n$addSelectMenuOption[Ejemplo;Primero;primera opción;La primera opción]\n$addSelectMenuOption[Ejemplo;Segundo;segunda-opción;La segunda opción]\n$addSelectMenuOption[Ejemplo;Tercero;tercera-opción;La tercera opción]"
        ],
        "images_example": [""],
        "deprecated":
        False,
    },
    "addTextInput": {
        "name":
        "$addTextInput[]",
        "tag":
        "$addTextInput[ID de entrada de texto;estilo;etiqueta;(longitud mínima;longitud;máxima;requerido?;valor;marcador de posición)]",
        "description":
        "Agrega una nueva entrada de texto a un modal.",
        "example": [
            "$nomention\n$newModal[modal;Biografía del usuario]\n$addTextInput[modalInput1;short;¿Cómo te llamas?;3;30;yes;;Mikołaj]\n$addTextInput[modalInput2;short;¿Cuáles son tus pronombres?;2;30;yes;;Él/Él]\n$addTextInput[modalInput3;paragraph;¿Puedes hablarnos de ti?;5;1000;no;;Soy desarrollador]"
        ],
        "images_example": [""],
        "deprecated":
        False,
    },
    "addTimestamp": {
        "name":
        "$addTimestamp[], $addTimestamp",
        "tag":
        "$addTimestamp[(Índice)]",
        "description":
        "Agrega una marca de tiempo a una inserción específica o embed, si no se proporciona nada se agrega la marca de tiempo a la primera insercción o embed.",
        "example": [
            "$nomention\n$description[¡Hola!]\n$description[¡Marca de tiempo!;2]\n$footer[Esa es la marca de tiempo =>;2]\n$addTimestamp[2]"
        ],
        "images_example": [
            f"{api}/funcion/images/addTimestamp.png"
        ],
        "deprecated":
        False,
    },
    "allMembersCount": {
        "name":
        "$allMembersCount",
        "tag":
        "$allMembersCount",
        "example":
        "$nomention\n¡Estoy atendiendo a usuarios de $allMembersCount!",
        "description": [
            "Devuelve el número total de usuarios de cada servidor en el que se encuentra el bot."
        ],
        "images_example": [
            f"{api}/funcion/images/allMembersCount.png"
        ],
        "deprecated":
        False,
    },
    "allowMention": {
        "name":
        "$allowMention",
        "tag":
        "$allowMention",
        "description":
        "Deshabilita el reemplazo de menciones en $message con texto.",
        "example": ["$nomention\n$allowMention\n$message"],
        "images_example": [
            f"{api}/funcion/images/allowMention.png"
        ],
        "deprecated":
        False,
    },
    "allowRoleMentions": {
        "name":
        "$allowRoleMentions[]",
        "tag":
        "$allowRoleMentions[ID de rol;...]",
        "description":
        "Habilita pings de roles solo para los ID de roles proporcionados, mientras que los roles no proporcionados serán \"ping falsos\" (se hará ping al rol, pero no se notificará a los usuarios).",
        "example": [
            "$nomention\n$allowRoleMentions[]\nEstoy haciendo ping <@&858376972303204362>, pero nadie recibió notificación; ¡Guau!"
        ],
        "images_example": [
            f"{api}/funcion/images/allowRoleMentions.png"
        ],
        "deprecated":
        False,
    },
    "allowUserMentions": {
        "name":
        "$allowUserMentions[]",
        "tag":
        "$allowRoleMentions[Usuario ID;..]",
        "description":
        "Permite pings de usuario solo para las ID de usuario proporcionadas, mientras que el usuario no proporcionado recibirá un \"ping falso\" (se hará ping al usuario, pero no se le notificará).",
        "example": [
            "$nomention\n$allowUserMentions[]\nHola <@$mentioned[1]>! Te mencioné, pero no te contactaron."
        ],
        "images_example": [
            f"{api}/funcion/images/allowRoleMentions.png"
        ],
        "deprecated":
        False,
    },
    "alternativePasing": {
        "name":
        "$alternativeParsing",
        "tag":
        "$alternativeParsing",
        "description":
        "Cambia la forma en que se leen los desencadenadores.",
        "example": [
            "$nomention\n$c[Este codigo se diferencia entre otros disparadores iguales.]\n$alternativeParsing\n$description[hello]",
            "$nomention\n$c[Este codigo no se diferenciara si tiene como disparadores otros comandos]\n$description[hola mundo!"
        ],
        "images_example": [
            f"{api}/funcion/images/alternativeParsing.png"
        ],
        "deprecated":
        False,
    },
    "and": {
        "name":
        "$and[]",
        "tag":
        "$and[Condicion;..]",
        "description":
        "Devuelve verdadero si todas las condiciones proporcionadas son verdaderas \";\" de lo contrario, devuelve falso.",
        "example":
        ["$nomention\n$and[$nickname==Euphoria;$message==Actualizacion]"],
        "images_example":
        [f"{api}/funcion/images/and.png"],
        "deprecated":
        False,
    },
    "argCount": {
        "name":
        "$argCount[]",
        "tag":
        "$argCount[Texto]",
        "description":
        "Devuelve cuántas palabras (también conocidas como argumentos) hay en el texto proporcionado.",
        "example": ["$nomention\nRecuento de palabras:$argCount[$message]"],
        "images_example": [
            f"{api}/funcion/images/argCount.png"
        ],
        "deprecated":
        False,
    },
    "argCheck": {
        "name":
        "$argCheck[]",
        "tag":
        "$argsCheck[¿cuántos?;mensaje de error]",
        "description":
        "Cuando se utiliza esta función, el comando solo se puede ejecutar si el mensaje del usuario contiene una cierta cantidad de argumentos (palabras).",
        "example": [
            "$nomention\n$argsCheck[>1;❌ ¡Por favor proporcione algo que pueda decir!]\n$noMensajeMensaje"
        ],
        "images_example": [
            f"{api}/funcion/images/argCheck.png"
        ],
        "deprecated":
        False,
    },
    "author": {
        "name":
        "$author[]",
        "tag":
        "$author[Texto;(Indice)]",
        "description":
        "Agrega texto del autor a una inserción o embed.",
        "example": ["$nomention\n$author[¡Este es el texto del autor!]"],
        "images_example": [
            f"{api}/funcion/images/author.png"
        ],
        "deprecated":
        False,
    },
    "authorAvatar": {
        "name":
        "$authorAvatar",
        "tag":
        "$authorAvatar",
        "description":
        "Devuelve la URL del avatar del autor.",
        "example":
        ["$nomention Tu avatar author $authorAvatar. $image[$authorAvatar]"],
        "images_example": [
            f"{api}/funcion/images/authorAvatar.png"
        ],
        "deprecated":
        False,
    },
    "authorIcon": {
        "name":
        "$authorIcon[]",
        "tag":
        "$authorIcon[URL;(Indice)]",
        "description":
        "Agrega un ícono a la sección del autor en la inserción.",
        "example": [
            "$nomention\n$authorIcon[$authorAvatar]\n$author[⬅️ Ese es el ícono de autor. Este es el texto del autor.]"
        ],
        "images_example": [
            f"{api}/funcion/images/authorIcon.png"
        ],
        "deprecated":
        False,
    },
    "authorID": {
        "name":
        "$authorID",
        "tag":
        "$authorID",
        "description":
        "Devuelve el ID del autor del mensaje.",
        "example": ["Autor tu id es $authorID"],
        "images_example": [
            f"{api}/funcion/images/authorID.png"
        ],
        "deprecated":
        False,
    },
    "authorOfMessage": {
        "name":
        "$authorOfMessage[]",
        "tag":
        "$authorOfMessage[ID de canal;ID de mensaje]",
        "description":
        "Devuelve el ID del autor del mensaje proporcionado.",
        "example": [
            "$nomention\nAutor del mensaje:\nEl author del mensaje es $username[$autorOfMessage[$message[1];$message[2]]]"
        ],
        "deprecated":
        False,
    },
    "authorURL": {
        "name":
        "$authorURL",
        "tag":
        "$authorURL[URL;(Indice)]",
        "description":
        "Agrega un hipervínculo al texto del author de la inserccion o embed.",
        "example": [
            "$nomention\n$author[Click par visitar la api de The BDS Word!]\n$authorURL[https://bdfd-function.lollol123yt.repl.co]"
        ],
        "deprecated":
        False,
    },
    "awaitFunc": {
        "name":
        "$awaitFunc[]",
        "tag":
        "$awaitFunc[nombre;(ID de usuario;ID de canal)]]",
        "description":
        "Se utiliza para iniciar un comando esperado.",
        "example": [
            "$nomention\n$c[El awaitFunc se complementa con el callblack awaitedCommand]\n¿Qué quieres que te diga\n$awaitFunc[decir]"
        ],
        "images_example": [],
        "deprecated":
        False,
    },
    "ban": {
        "name":
        "$ban[], $ban",
        "tag":
        "$ban[(Razon)]",
        "description":
        "Banea a un usuario del servidor con una razon.",
        "example": [
            "$nomention\n$ban[$noMentionMessage]\n<@$mentioned[1]> ha sido baneado correctamente"
        ],
        "images_example":
        [f"{api}/funcion/images/ban.png"],
        "deprecated":
        False,
    },
    "banID": {
        "name":
        "$banID[], $banID",
        "tag":
        "$banID[Razon;(ID de usuario)]",
        "description":
        "Prohíbe a un usuario usar su ID.",
        "example": [
            "$nomention\n$banID[$message[1];$message[2]]\n<@$message[1]> Ha sido baneado correctamente por la razon de $message[2]"
        ],
        "images_example":
        [f"{api}/funcion/images/banID.png"],
        "deprecated":
        False
    },
    "blackListIDs": {
        "name":
        "$blackListIDs[]",
        "tag":
        "$blackListIDs[ID de usuario;..;Mensaje de error.]",
        "description":
        "Bloquea a ciertos usuarios para que no utilicen el comando.",
        "example": [
            "$nomention\n$blackListIDs[566613317972394004;437154602626973697;¡No puedes usar este comando!]\n¡Hola! $nickname"
        ],
        "images_example": [
            f"{api}/funcion/images/blackListIDs.png"
        ],
        "deprecated":
        False
    },
    "blackListRoles": {
        "name":
        "$blackListRoles[]",
        "tag":
        "blackListRoles[Nombre del rol;...;Mensaje de error.]",
        "description":
        "Bloquea a los usuarios con ciertos roles para que no utilicen el comando. Si el usuario tiene algún rol en la lista negra, no podrá ejecutar el comando. Utiliza nombres de funciones en lugar de ID de funciones.",
        "example": [
            "$nomention\n$blackListRoles[Owner;Bot;❌ ¡No puedes usar este comando!]\nPong! $ping ms"
        ],
        "images_example": [],
        "deprecated":
        False
    },
    "blackListRolesIDs": {
        "name":
        "$blackListRolesIDs[]",
        "tag":
        "blackListRolesIDs[ID de un rol;...;Mensaje de error]",
        "description":
        "Bloquee a los usuarios con ciertos roles para que no utilicen el comando. Si el usuario tiene algún rol en la lista negra, no podrá ejecutar el comando.",
        "example": [
            "$nomention\n$blackListRolesIDs[1009019299987476540;1014547313957539901;❌ ¡No puedes usar este comando!]\n¡Apestar! $ping ms"
        ],
        "images_example": [
            f"{api}/funcion/images/blackListRolesIDs.png"
        ],
        "deprecated":
        False
    },
    "blackListServers": {
        "name":
        "$blackListServers[]",
        "tag":
        "$blackListServers[ID de un servidor;...;Mensaje de error]",
        "description":
        "Deshabilita este comando para los servidores proporcionados.",
        "example": [
            "$nomention\n$blackListServers[1009018669982031912;❌ ¡No puedes usar este comando!]\n**¡Hola $username!**\n*ID del gremio: $guildID*"
        ],
        "images_example": [
            f"{api}/funcion/images/blackListServers-1.png",
            f"{api}/funcion/images/blackListServers-2.png"
        ],
        "deprecated":
        False
    },
    "blackListUsers": {
        "name":
        "$blackListUsers[]",
        "tag":
        "$blackListUsers[Nombre de usuario;...;Mensaje de error.]",
        "description":
        "Deshabilita el comando para usuarios con nombres de usuario que coincidan con los proporcionados.",
        "example": [
            "$nomention\n$blackListUsers[RainbowKey;❌ ¡No puedes usar este comando!]\nHola $nombre de usuario!"
        ],
        "images_example": [],
        "deprecated":
        False
    },
    "boostCount": {
        "name":
        "$boostCount[]",
        "tag":
        "$boosCount[(ID de servidor)]",
        "description":
        "Devuelve el número de potenciadores de nitro del servidor.",
        "example": [
            "$nomention\nEste servidor actualmente tiene impulso(s) de $boostCount[$guildID]."
        ],
        "images_example": [],
        "deprecated":
        False
    },
    "botCommands": {
        "name": "$botCommands[]",
        "tag": "$botCommand[Separador]",
        "description": "Devuelve una lista de los comandos del bot.",
        "example": ["Todos los comando del bot:\n$botCommands[\n]"],
        "images_example": [""],
        "deprecated": False
    },
    "botID": {
        "name": "$botID",
        "tag": "$botID",
        "description": "Devuelve la identificación o ID del bot.",
        "example": ["Mi ID es :\n$botID"],
        "images_example": [""],
        "deprecated": False
    },
    "botLeave": {
        "name":
        "$botLeave[]",
        "tag":
        "$botLeave[(ID de servidor)]",
        "description":
        "El bot se ve obligador a abandonar el gremio o servidor.",
        "example": [
            "$nomention\n$sendMessage[¡Dejé este servidor!]\n$botLeave[$guildID]"
        ],
        "images_example": [""],
        "deprecated":
        False
    },
    "botListDescription": {
        "name": "$botListDescription[]",
        "tag": "$botListDescription[Texto]",
        "description":
        "Establece la descripción de este comando para la lista de comandos BDL (si el bot está en la lista de Bot Designer: https://botdesignerlist.com).",
        "example": ["$nomention\n¡Pong!n\n$botListDescription[¿Ping? ¡Pong!]"],
        "images_example": [""],
        "deprecated": False
    },
    "botListHide": {
        "name": "$botListHide",
        "tag": "$botListHide",
        "description":
        "Oculta este comando para que no se muestre en la lista de comandos BDL (si el bot está en la lista de Bot Designer: https://botdesignerlist.com).",
        "example":
        ["$nomention\n¡Este es un comando secreto! 🤫\n$botListHide"],
        "images_example": [""],
        "deprecated": False
    },
    "botNode": {
        "name":
        "$botNode",
        "tag":
        "$botNode",
        "description":
        "Devuelve el nodo en el que se encuentra el bot",
        "example": ["Me encuentro en el nodo: $botNode"],
        "images_example": [
            f"{api}/funcion/images/botNode.png"
        ],
        "deprecated":
        False
    },
    "botOwnerID": {
        "name":
        "$botOwnerID",
        "tag":
        "$botOwnerID",
        "description":
        "Devuelve la identificacion o ID del dueño del bot.",
        "example": ["$nomention'nEl ID del dueño del bot es: $botOwnerID"],
        "images_example": [
            f"{api}/funcion/images/botOwnerID.png"
        ],
        "deprecated":
        False
    },
    "botTyping": {
        "name":
        "$botTyping",
        "tag":
        "$botTyping",
        "description":
        "Esta función le dice a Discord que el bot está escribiendo.",
        "example": ["$nomention\n$botTyping\n¡Escribiendo!"],
        "images_example": [
            f"{api}/funcion/images/botTyping-1.png",
            f"{api}/funcion/images/botTyping-2.png"
        ],
        "deprecated":
        False
    },
    "c": {
        "name":
        "$c[]",
        "tag":
        "$c[Texto]",
        "description":
        "Agrega un comentario al código. Los comentarios no aparecen en la respuesta del bot.",
        "example": [
            "$nomention\n$c[Este mensaje no se mostrara]\nEste mensaje si se mostrará"
        ],
        "images_example":
        [f"{api}/funcion/images/c.png"],
        "deprecated":
        False
    },
    "calculate": {
        "name":
        "$calculate[]",
        "tag":
        "$calculate[Expresion]",
        "description":
        "Calcula una expresion matematica",
        "example": ["$nomention\nEl resultado de 1+1 es: $calculate[1+1]"],
        "images_example": [
            f"{api}/funcion/images/calculate.png"
        ],
        "deprecated":
        False
    },
    "categoryChannels": {
        "name":
        "$categoryChannels[]",
        "tag":
        "$categoryChannels[ID de categoría;separador;(opción)]",
        "description":
        "Enumere la propiedad del canal en una categoría determinada.",
        "example":
        ["$nomention\n<#$categoryChannels[$categoryID[ADMIND ZONE];\n<#;id]>"],
        "images_example": [
            f"{api}/funcion/images/categoryChannels.png"
        ],
        "deprecated":
        False
    },
    "categoryCount": {
        "name":
        "$categoryCount[]",
        "tag":
        "$categoryCount[(ID de un servidor)]",
        "description":
        "Devuelve el recuento de categorías del gremio o ID del servidor proporcionado.",
        "example": [
            "$nomention\n¡Hay categorías $categoryCount[$guildID] en el servidor!"
        ],
        "images_example": [
            f"{api}/funcion/images/categoryCount.png"
        ],
        "deprecated":
        False
    },
    "cateforyID": {
        "name":
        "%categoryID[], $categoryID",
        "tag":
        "$categoryID[Nombre de una categoria]",
        "description":
        "Devuelve el ID de categoría para el nombre de categoría determinado.",
        "example": ["$nomentio\nID de categoría: $categoryID[admind zone]"],
        "images_example": [
            f"{api}/funcion/images/categoryID.png"
        ],
        "deprecated":
        False,
    },
    "changeCooldownTime": {
        "name":
        "$changeCooldownTimes[]",
        "tag":
        "$changeCooldownTimes[días;horas;minutos;segundos]",
        "description":
        "Cambia las métricas de tiempo de reutilización. Estos se pueden utilizar en mensajes de error de tiempo de reutilización. Puede resultar útil para las traducciones.",
        "example": [
            "$nomention\nHola $nombre de usuario!\n$changeCooldownTime[Días⏰;Horas⏰;Minutos🕧;Segs🕧]\n$cooldown[10m;¡Espere %time-m%!]"
        ],
        "images_example": [
            f"{api}/funcion/images/changeCooldownTime.png"
        ],
        "deprecated":
        False,
    },
    "changeUsername": {
        "name":
        "$changeUsername[]",
        "tag":
        "$changeUsername[Nuevo apodo]",
        "description":
        "Cambia el apodo del usuario mencionado.",
        "example": [
            "$nomention\n$onlyPerms[managenicknames;¡Falta el permiso 'administrar apodos'!]\n$argsCheck[>2;¡Uso incorrecto! Uso correcto: `!apodo (usuario) (texto)`]\n$changeUsername[$noMentionMessage]\nSe cambió el apodo de <@$mentioned[1]> a `$noMentionMessage`."
        ],
        "images_example": [
            f"{api}/funcion/images/changeUsername.png"
        ],
        "deprecated":
        False,
    },
    "changeUsernameWithID": {
        "name":
        "$changeUsernameWithID[]",
        "tag":
        "$changeUsernameWithID[ID de usuario;Nuevo apodo]",
        "description":
        "Cambia el apodo de un usuario usando su ID.",
        "example": [
            "$nomention $argsCheck[>1;¡Por favor proporcione texto!] $addCmdReactions[✅]\nCompletado de cambio el apodo a <@$message[1]> \n$changeUsernameWithID[$findUser[$message[1]];$message[2]]"
        ],
        "images_example": [
            f"{api}/funcion/images/changeUsernameWithID.png"
        ],
        "deprecated":
        False,
    },
    "channelCount": {
        "name":
        "$chhanelCount",
        "tag":
        "$chaannelCount",
        "description":
        "Devuelve la cantidad de canales en el servidor actual.",
        "example":
        ["$nomention\n¡Hay $channelCount canales en este servidor!"],
        "images_example": [
            f"{api}/funcion/images/channelCount.png"
        ],
        "deprecated":
        False,
    },
    "channelExists": {
        "name":
        "$channelExists[]",
        "tag":
        "$channelExists[ID de canal]",
        "description":
        "Comprueba si el canal proporcionado existe en algún servidor en el que se encuentre el bot.",
        "example": ["$nomention\n$channelExists[$message]"],
        "images_example": [
            f"{api}/funcion/images/channelCount.png"
        ]
    },
    "channelID": {
        "name":
        "$channelID[], $channelID",
        "tag":
        "$channelID[(Nombre de canal)]",
        "description":
        "Devuelve ID del canal donde se ejecuta el comando, si se proporciona un nombre de un canal devuelve su identificacion o ID de este.",
        "example": ["$nomention\nID de canal: $channelID[$mensaje]"],
        "images_example": [
            f"{api}/funcion/images/channelID.png"
        ],
        "deprecated":
        False,
    },
    "channelIDFromName": {
        "name":
        "$channelIDFromName[]",
        "tag":
        "$channelIDFromName[Nombre de un canal]",
        "description":
        "Devuelve el ID de un canal a partir de su nombre.",
        "example": ["$nomencion\nID del canal: $channelIDFromName[$mensaje]"],
        "images_example": [
            f"{api}/funcion/images/channelIDFromName.png"
        ],
        "deprecated":
        True,
    },
    "channelName": {
        "name":
        "$channelName[]",
        "tag":
        "$channelName[Nombre del canal]",
        "description":
        "Devuelve el nombre del ID del canal proporcionado.",
        "example":
        ["$nomentio\nNombre del canal: <#$channelName[$channelID]>"],
        "images_example": [
            f"{api}/funcion/images/channelName.png"
        ],
        "deprecated":
        False
    },
    "channelNames": {
        "name":
        "$channelNames[]",
        "tag":
        "$channelNames[Sepador;(ID de un servidor)]",
        "description":
        "Enumere todos los nombres de canales separados por un separador determinado.",
        "example": ["$nomention\n#$channelNames[\n#]"],
        "images_example": [
            f"{api}/funcion/images/channelNames.png"
        ],
        "deprecated":
        False
    },
    "channelPosition": {
        "name":
        "$channelPosition[], $channelPosition",
        "tag":
        "$channelPosition[(ID de un canal)]",
        "description":
        "Devuelve la posición del canal actual o la Indentificacion de un canal proporcionado.",
        "example":
        ["$nomention La posicion del canal es : $channelPosition[$channelID]"],
        "images_example": [
            f"{api}/funcion/images/channelPosition.png"
        ],
        "deprecated":
        False
    },
    "channelSendMessage": {
        "name":
        "$channelSendMessage[]",
        "tag":
        "$channelSendMessage[ID de un canal;Texto]",
        "description":
        "Envía un mensaje en el canal proporcionado.",
        "example": [
            "$nomention\n$channelSendMessage[$channelID;Hola este es un mensaje]\nCompletado."
        ],
        "images_example": [
            f"{api}/funcion/images/channelSendMessage-1.png",
            f"{api}/funcion/images/channelSendMessage-2.png"
        ],
        "deprecated":
        False
    },
    "channelTopic": {
        "name":
        "$channelTopic[], $channelTopic",
        "tag":
        "$channelTopic[(ID de canal)]",
        "description":
        "Devuelve el tema del canal en el que se utiliza el comando o devuelve el tema del canal proporcionado.",
        "example":
        ["$nomention\nEl tema del canal de <#$channelID> es: $channelTopic"],
        "images_example": [
            f"{api}/funcion/images/channelTopic.png"
        ],
        "deprecated":
        False
    },
    "channelType": {
        "name": "$channeltype[]",
        "tag": "$channeType[Canal ID]",
        "description":
        "Devuelve el tipo de canal con el ID de canal proporcionado ",
        "example": ["$nomention\n $channelType[$channelID] "],
        "images_example": [],
        "deprecated": False
    },
    "charCount": {
        "name":
        "$charCount[]",
        "tag":
        "$charCount[Texto]",
        "description":
        "Devuelve la cantidad de caracteres del \"Texto\" proporcionado.",
        "example":
        ["$nomention\nSu mensaje tiene: **$charCount[$message]** caracteres."],
        "images_example": [
            f"{api}/funcion/images/checkCondition.png"
        ],
        "deprecated":
        False
    },
    "checkCondition": {
        "name":
        "$checkCondition[]",
        "tag":
        "$checkCondtion[Condicion]",
        "description":
        "Comprueba si una condición es true(verdadera) o false(falsa). ",
        "example": [
            "$nomention\nEl apodo del author es Euphoria? $checkCondition[$nickname==Euphoria]"
        ],
        "images_example": [
            f"{api}/funcion/images/checkCondition.png"
        ],
        "deprecated":
        False
    },
    "checkContains": {
        "name":
        "$checkContains[]",
        "tag":
        "$checkContains[Texto;Frases]",
        "description":
        "Comprueba si el 'texto' contiene al menos una de las 'frases' proporcionadas.",
        "examples": ["$nomention\n$checkContains[$message;hey;hola]"],
        "images_example": [
            f"{api}/funcion/images/checkContains.png"
        ],
        "deprecated":
        False
    },
    "checkUserPerms": {
        "name":
        "$checkUserPerms[]",
        "tag":
        "$checkUserPerms[ID de usuario;permisos]",
        "description":
        "Devuelve \"verdadero\" si un usuario tiene todos los permisos proporcionados; de lo contrario, devuelve \"falso\".",
        "example":
        ["$nomention\nTengo administrador?: $checkUserPerms[$authorID;admin]"],
        "images_example": [
            f"{api}/funcion/images/checkUserPerms.png"
        ]
    },
    "clear": {
        "name":
        "$clear[], $clear",
        "tag":
        "$clear[Cantidad;(ID de usuario;¿Eliminar mensajes fijados?)]",
        "description":
        "Elimina la cantidad proporcionada de mensajes.",
        "example": [
            "$nomention\n$onlyPerms[managemessages;¡Necesitas el permiso 'MANAGE_MESSAGES' para usarlo!]\n$argsCheck[>1;Indique cuántos mensajes desea borrar. Uso: !purge (número)]\nSe eliminaron la cantidad de $message de mensajes.\n$clear[$message]"
        ],
        "images_example":
        [f"{api}funcion/images/clear.png"],
        "deprecated":
        False
    },
    "clearReactions": {
        "name":
        "$clearReactions[]",
        "tag":
        "$clearReactions[ID de canal;ID de mensaje;emoji]",
        "description":
        "Elimina reacciones del mensaje proporcionado.",
        "example": [
            "$nomention\nSe Se elimino el emoji $message[2] del mensaje.\n$clearReactions[$channelID;$message[1];$message[2]]"
        ],
        "images_example": [
            f"{api}/funcion/images/clearReactions.png"
        ],
        "deprecated":
        False
    },
    "closeTicket": {
        "name":
        "$closeTicket[]",
        "tag":
        "$closeTicket[Mensaje de error]",
        "description":
        "Elimina el canal del ticket (debe crearse con $newTicket).",
        "example": ["$nomention\n$closeTicket[¡Ese canal no es un ticket!]"],
        "images_example": [
            f"{api}/funcion/images/closeTicket.png"
        ],
        "deprecated":
        False
    },
    "color": {
        "name":
        "$color[]",
        "tag":
        "$color[Color Hexadecimal;(Indice)]",
        "description":
        "Establece el color del borde de inserción o embed.",
        "example": [
            "$nomention\n$description[⬅️ El color del embed que tiene como #4153f1]\n$color[#4153f1]"
        ],
        "images_example":
        ["https://bdfd-function.lollol123yt.repl.co/funcion/images/color.png"],
        "deprecated":
        False
    },
    "colorRole": {
        "name":
        "$colorRole[]",
        "tag":
        "$colorRole[Color hexadecimal]",
        "description":
        "Cambiar el color del rol mencionado.",
        "example": [
            "$onlyPerms[manageroles;¡Necesitas el permiso de Manage_roles para usarlo!]\n$argsCheck[>2;¡Proporcione los argumentos necesarios! Los argumentos `colorHexadecimal` y `rol` son necesarios.]\n$colorRole[$noMentionMessage]\n✅ ¡Cambió el color del rol!"
        ],
        "images_example": [
            "https://bdfd-function.lollol123yt.repl.co/funcion/images/colorRole.png"
        ],
        "deprecated":
        False
    },
    "commandsCount": {
        "name":
        "$commandsCount",
        "tag":
        "$commandsCount",
        "description":
        "Devuelve cuántos comandos tiene el bot en total.",
        "example": ["Yo tengo $commandsCount de comandos"],
        "images_example": [
            "https://bdfd-function.lollol123yt.repl.co/funcion/images/commandsCount.png"
        ],
        "deprecated":
        False
    },
    "cooldown": {
        "name":
        "$cooldown[]",
        "tag":
        "$cooldown[Duración;Mensaje de error]",
        "description":
        "Establece un tiempo de reutilización. El usuario no puede volver a ejecutar el comando hasta que se acabe la 'duración'.",
        "example": [
            "$nomention\n$cooldown[30s;¡Espere %time% y luego use ese comando nuevamente!]\n¡Hola!"
        ],
        "images_example": [
            "https://bdfd-function.lollol123yt.repl.co/funcion/images/cooldown.png"
        ],
        "deprecated":
        False
    },
    "createChannel": {
        "name":
        "$createChannel[]",
        "tag":
        "$createChannel[Nombre;Tipo;(ID de categoria)]",
        "description":
        "Crea un canal fuera de todas categorias de contrario si usa el tercer argumento se crea el canal en la ID categoria proporcionada",
        "example": ["$nomention\n$createChannel[mod-logs];text]"],
        "images_example": [
            "https://bdfd-function.lollol123yt.repl.co/funcion/images/createChannel-1.png",
            "https://bdfd-function.lollol123yt.repl.co/funcion/images/createChannel-2.png"
        ],
        "deprecated":
        False
    },
    "createRole": {
        "name":
        "$createRole[]",
        "tag":
        "$createRole[Nombre del rol;Color hexadecimal;¿Elevador?;¿Mencionable?]",
        "description":
        "Crea un nuevo en el servidor",
        "example": [
            "$nomention\n$createRole[Rol genial;#FFFF00;yes;no]\b¡Creado nuevo rol!"
        ],
        "images_example": [
            f"{api}funcion/images/createRole-1.png",
            f"{api}funcion/images/createRole-2.png"
        ],
        "deprecated":
        False
    },
    "creationDate": {
        "name":
        "$creationDate[]",
        "tag":
        "$creationDate[ID;(formato)]]",
        "description":
        "Devuelve la fecha de creación de cualquier ID de Discord Snowflake válida.",
        "example": [
            "$nomention\n$creationDate[$authorID]",
            "$nomention\n$creationDate[$authorID;January 2, 2006 at 3:04 PM (MST -07:00)]"
        ],
        "images_example": [
            f"{api}/funcion/images/creationDate-1.png",
            f"{api}/funcion/images/creationDate-2.png"
        ],
        "deprecated":
        False
    },
    "cropText": {
        "name":
        "$cropText[]",
        "tag":
        "$cropText[Texto;Caracteres máximos;final]",
        "description":
        "Recorta el texto proporcionado. Si el texto se recorta, el `final` se agrega al final del texto.",
        "example": ["$nomention\n$cropText[Hola como estas;4;...]"],
        "images_example": [
            f"{api}/funcion/images/cropText.png"
        ],
        "deprecated":
        False
    },
    "customEmoji": {
        "name":
        "$customEmoji[]",
        "tag":
        "$customEmoji[Nombre de emoji]",
        "description":
        "Retorna un emoji customizable.",
        "example": ["$nomention\n¡Hola! $customEmoji[wumpus]"],
        "images_example": [
            f"{api}/funcion/images/customEmoji.png"
        ],
        "deprecated":
        False
    },
    "customID": {
        "name":
        "$customID",
        "tag":
        "$customID",
        "description":
        "Solo se puede utilizar con la devolución de llamada `$onInteraction`. Devuelve el ID personalizado de esta interacción.",
        "example": [
            "$nomention\n$c[Este codigo representa la interaccion que hara con customID en el boton y este lleva de prefix: $onInteracion como se menciono.]\n$if[$customID==button1-$authorID]\n$editButton[$customID;Boton presionado;success;yes;]\n$endif"
        ],
        "images_example": [
            f"{api}/funcion/images/customID.png"
        ],
        "deprecated":
        False
    },
    "date": {
        "name":
        "$date",
        "tag":
        "$date",
        "description":
        "Devuelve la fecha actual.",
        "example": ["La fecha es: $date"],
        "images_example":
        [f"{api}/funcion/images/date.png"],
        "deprecated":
        False
    },
    "day": {
        "name":
        "$day",
        "tag":
        "$day",
        "description":
        "Devuelve el día actual del mes.\n🧙‍♂️ Puedes usar $time para cambiar la zona horaria.",
        "example": ["El dia es: $day"],
        "images_example":
        [f"{api}/funcion/images/day.png"],
        "deprecated":
        False
    },
    "defer": {
        "name":
        "$defer",
        "tag":
        "$defer",
        "description":
        "Retrasa la respuesta a una interacción de componentes o botones y comandos de barra diagonal o slash, el tiempo sera dependiendo cuan pesado sea el codigo.",
        "example": ["$nomention\n$defer\n$message[message-id]"],
        "images_example":
        [f"{api}/funcion/images/defer.gif"],
        "deprecated":
        False
    },
    "deleteChannels": {
        "name":
        "$deleteChannels[]",
        "tag":
        "$deleteChannels[ID de canal;...]",
        "description":
        "Elimina los canales propocionados",
        "example": [
            "$nomention\nCanal eliminado: <#$mentionedChannels[1]>\n$deleteChannels[$mentionedChannels[1]]"
        ],
        "images_example": [
            f"{api}/funcion/images/deleteChannels.png"
        ],
        "deprecated":
        False
    },
    "deleteChannelsByName": {
        "name":
        "deleteChannelsByName[]",
        "tag":
        "deleteChannelsByName[Nombre de canal;..]",
        "description":
        "Elimina todos los canales que coincidan con los nombres proporcionados.",
        "example": [
            "$nomention\n$argsCheck[>1;¡Por favor proporcione un nombre de canal!]\n$onlyPerms[managechannels;❌ ¡Necesitas el permiso `MANAGE_CHANNELS` para usarlo!]\¡Eliminó exitosamente el canal #$channelName[$channelID[$message]]!\n$deleteChannelsByName[$mensaje]"
        ],
        "images_example": [
            f"{api}/funcion/images/deleteChannelsByName.png"
        ],
        "deprecated":
        False
    },
    "deletecommand": {
        "name":
        "$deletecommand",
        "tag":
        "$deletecommand",
        "description":
        "Elimina el mensaje de comando del autor.",
        "example": ["$nomention\n$deletecommand\nHola $username"],
        "images_example": [
            f"{api}/funcion/images/deletecommand.png"
        ],
        "deprecated":
        False
    },
    "deleteIn": {
        "name":
        "$deleteIn[]",
        "tag":
        "$deleteIn[Tiempo]",
        "description":
        "Elimina la respuesta del bot después de la duración proporcionada.",
        "example": ["$nomention\nHello World!\n$deleteIn[3s]"],
        "images_example": [
            f"{api}/funcion/images/deleteIn.png"
        ],
        "deprecated":
        False
    },
    "deleteMessage": {
        "name":
        "$deleteMessage[]",
        "tag":
        "$deleteMessage[Canal ID;Mensaje ID]",
        "description":
        "Elimina un mensaje.",
        "example": [
            "$nomention\n$c[Este codig eliminara el dispador con el que se activo el comando]\n$deleteMessage[$channelID;$messageID]\nHola $username!"
        ],
        "images_example": [
            f"{api}/funcion/images/deleteMessage.png"
        ],
        "deprecated":
        False
    },
    "deleteRole": {
        "name":
        "$deleteRole[]",
        "tag":
        "$deleteRole[ID de rol]",
        "description":
        "Elimina un rol.",
        "example": ["$nomention\nRol eliminado \n$deleteRole[$message[1]]"],
        "images_example": [
            f"{api}/funcion/images/deleteRole-1.png",
            f"{api}/funcion/images/deleteRole-2.png"
        ],
        "deprecated":
        False
    },
    "description": {
        "name":
        "$description[]",
        "tag":
        "$description[Texto;(Indice)]",
        "description":
        "Agrega una descripcion a la inserccion o embed",
        "example": ["$nomention\n$description[¡Esta es una descripción! 😎]"],
        "images_example": [
            f"{api}/funcion/images/description.png"
        ],
        "deprecated":
        False
    },
    "disableInnerSpaceRemoval": {
        "name":
        "$disableInnerSpaceRemoval",
        "tag":
        "$disableInnerSpaceRemoval",
        "description":
        "Desactiva la eliminación de múltiples espacios dentro del mensaje.",
        "example": [
            "$nomention\n$c[Con la funcion ]\n$disableInnerSpaceRemoval\nHola               $username!",
            "$nomention\n$c[Sin funcion]\nHola               $username!"
        ],
        "images_example": [
            f"{api}/funcion/images/disableInnerSpaceRemoval-1.png",
            f"{api}/funcion/images/disableInnerSpaceRemoval-2.png"
        ],
        "deprecated":
        False
    },
    "disableSpecialEscaping": {
        "name":
        "$disableSpecialEscaping",
        "tag":
        "$disableSpecialEscaping",
        "description":
        "Desactiva el escape para `;` y `$` (por ejemplo, `%{-EMICOL-}%` se interpreta como un normal `;`).",
        "example": [
            "$nomention\n$c[La palabra es \"SEMICOL\", por bdfd no se puede dar el ejemplo bien.]\n\n$disableEscapeEspecial\n%{DOL}%replaceText[¡Hola planeta!%{-EMICOL-}%planeta%{-EMICOL-}%mundo%{-EMICOL-}%1]"
        ],
        "images_example": [
            f"{api}/funcion/images/disableSpecialEscaping.png"
        ],
        "deprecated":
        False
    },
    "discriminator": {
        "name":
        "$descriminator[]",
        "tag":
        "$descriminator[Usuario ID]",
        "description":
        "Devuelve el discriminador de un usuario (el número de 4 dígitos al final de su nombre de usuario).",
        "example": [
            "$nomention\nHola soy, $username[$authorID]#$discrminator[$authorID]!"
        ],
        "images_example": [
            f"{api}/funcion/images/discriminator.png"
        ],
        "deprecated":
        True
    },
    "displayName": {
        "name":
        "$displayName[], $displayName",
        "tag":
        "$displayName[Usuario ID]",
        "description":
        "Devuelve el nombre del usuario proporcionado o del author(Solo si nose abre sus corchetes).",
        "example": [
            "$nomention\nEl nombre para mostrar de **$username[$message[1]]** es `$displayName[$message[1]]`\nEl tuyo es `$displayName`"
        ],
        "images_example": [
            f"{api}/funcion/images/displayName.png"
        ],
        "deprecated":
        False
    },
    "divide": {
        "name":
        "$divide[]",
        "tag":
        "$divide[Numero;...]",
        "description":
        "Divide los números proporcionados.",
        "example": [
            "$nomention\n$argsCheck[>2;❌ ¡Proporcione los argumentos necesarios! Uso: `!dividir (número1) (número2)`]\nRespuesta: $divide[$mensaje[1];$mensaje[2]]"
        ],
        "images_example": [
            f"{api}/funcion/images/divide.png"
        ],
        "deprecated":
        False
    },
    "dm": {
        "name":
        "$dm[], $dm",
        "tag":
        "$dm[Ususario ID;...]",
        "description":
        "Mensajes directos al usuario que ejecuta el comando.",
        "example": [
            "$nomention\n$dm[]\n$displayName saluda 👋",
            "$nomention\n$dm\nHola $username"
        ],
        "images_example": [
            f"{api}/funcion/images/dm-1.png",
            f"{api}/funcion/images/dm-2.png"
        ],
        "deprecated":
        False
    },
    "dmChannelID": {
        "name":
        "$dmChannelID[]",
        "tag":
        "$dmChannelID[Usuario ID]",
        "description":
        "Recupera el ID del canal DM para el ID de usuario proporcionado.",
        "example": ["$nomention\nID: $dmChannelID[$auhorID"],
        "images_example": [
            f"{api}/funcion/images/dmChannelID.png"
        ],
        "deprecated":
        False
    },
    "editButton": {
        "name":
        "$editButton[]",
        "tag":
        "$editButton[ID/URL del botón;Etiqueta;Estilo;(Deshabilitado;Emoji;ID del mensaje)]",
        "description":
        "Edita un botón ya existente.",
        "example": [
            "$nomention$username Di hola!!\n$editButton[test;Di Hola!;primary;yes;]\n$addButton[false;https://bdfd-function.lollol123yt.repl.co;Checa nuestra API;link;false;👀]"
        ],
        "images_example": [
            f"{api}/funcion/images/editButton.png"
        ],
        "deprecated":
        False
    },
    "editChannelsPerms": {
        "name":
        "$editChannelsPerms[]",
        "tag":
        "$editChannelsPerms[ID de canal;ID de usuario/rol;Permiso;...]",
        "description":
        "Cambia los permisos para el usuario/rol mencionado en el canal proporcionado.",
        "example": [
            "$nomention\n$onlyPerms[managechannels;❌ ¡Necesitas el permiso `MANAGE_CHANNELS` para usarlo!]\n$editChannelPerms[$channelID;$mentionedRoles[1];-sendmessages]\n✅ Ahora el rol no puede enviar mensajes"
        ],
        "images_example": [
            f"{api}/funcion/images/editChannelsPerms.png"
        ],
        "deprecated":
        False
    },
    "editEmbedIn": {
        "name":
        "$editEmbedIn[]",
        "tag":
        "$editEmbedIn[Tiempo;(Título;Descripción;Pie de página;Color hexadecimal)]",
        "description":
        "Edita el mensaje del bot después del tiempo indicado, como una inserción.",
        "example": [
            "$nomention\$title[Titulo genial]\n$description[¡Esta es una inserción genial para editar!]\n$color[#6A96FC]\n$editEmbedIn[5s;Título épico;¡Esta es la descripción editada!;;#E46AFC]"
        ],
        "images_example": [
            f"{api}/funcion/images/editEmbedIn-1.png",
            f"{api}/funcion/images/editEmbedIn-2.png"
        ],
        "deprecated":
        False
    },
    "editIn": {
        "name":
        "editIn[]",
        "tag":
        "editIn[Tiempo;Mensaje]",
        "description":
        "Edita la respuesta del bot después del tiempo indicado.",
        "example": [
            "$nomention\n¡Este es un buen mensaje para editar!\n$editIn[5s;¡Este es el mensaje editado!]"
        ],
        "images_example": [
            f"{api}/funcion/images/editIn-1.png",
            f"{api}/funcion/images/editIn-2.png"
        ],
        "deprecated":
        False
    },
    "editMessage": {
        "name":
        "$editMessage[]",
        "tag":
        "$editMessage[ID de canal;ID de mensaje;Contenido;(Título;Descripción;Color hexadecimal;Pie de página)]",
        "description":
        "Edita uno de los mensajes del bot.",
        "example": [
            "$nomention\n$editMessage[$channelID;$message[1];Este mensaje a sido editado!]"
        ],
        "images_example": [
            f"{api}/funcion/images/editMessage-2.png",
            f"{api}/funcion/images/editMessage-1.png"
        ],
        "deprecated":
        False
    },
    "editSelectMenu": {
        "name":
        "$editSelectMenu[]",
        "tag":
        "$editSelectMenu[ID de menú;Min;Max;(Marcador de posición;ID de mensaje)]",
        "description":
        "Edita un menú de selección. ",
        "example": [
            "$nomention\n$editSelectMenu[Ejemplo;1;1;Elija alguna opción 😀]\n$addSelectMenuOption[Ejemplo;Primero;primera opción;La primera opción]\n$addSelectMenuOption[Ejemplo;Segundo;segunda-opción;La segunda opción]\n$addSelectMenuOption[Ejemplo;Tercero ;tercera-opción;La tercera opción] "
        ],
        "images_example": [""],
        "deprecated":
        False
    },
    "editSelectMenuOption": {
        "name":
        "$editSelectMenuOption[]",
        "tag":
        "$editSelectMenuOption[ID de opción de menú;Etiqueta;Valor;Descripción;(Predeterminado;Emoji;ID de mensaje)]",
        "description":
        "Edita una opción del menú de selección.",
        "example": [
            "$nomention\n$editSelectMenuOption[Ejemplo;Primero;primera opción;La primera opción;false;1️⃣]\n$editSelectMenuOption[Ejemplo;Segundo;segunda-opción;La segunda opción;false;2️⃣]\n$editSelectMenuOption[Ejemplo;Tercero;tercera-opción;El tercera opción;false;3️⃣]"
        ],
        "images_example": [""]
    },
    "editSplitText": {
        "name":
        "$editSplitText[]",
        "tag":
        "$editSplitText[Índice;Valor]",
        "description":
        "Edita un elemento de texto dividido utilizando su índice.",
        "example": [
            "$nomention\n$textSplit[$mensaje; ]\n$var[Index;$splitText[$sub[$getTextSplitLength;1]]]\n$var[Value;$splitText[$getTextSplitLength]]\n$removeSplitTextElement[$getTextSplitLength]\n$removeSplitTextElement[$getTextSplitLength]\n$var[Texto;$joinSplitText[ ]]\n$textSplit[$var[Texto];] \n$editSplitText[$var[Index];$var[Value]]\nTexto original: $var[Texto]\nNuevo texto: $joinSplitText[]"
        ],
        "images_example": [""],
        "deprecated":
        False
    },
    "editThread": {
        "name":
        "$editThread[]",
        "tag":
        "$editThread[ID del hilo;(Nombre;Archivado;Duración del archivo;Bloqueado;Modo lento)]",
        "description":
        "Modifica un hilo existente. ",
        "example": [
            "$nomention\n$editThread[1098166444111433819;hilo genial 😎;false;!unchanged;!unchanged;5] "
        ],
        "imgaes_example": [""],
        "deprecated":
        False
    },
    "else": {
        "name":
        "$else",
        "tag":
        "$else",
        "description":
        "Un bloque de código que se ejecutará si la condición `$if[]` es falsa.",
        "example": [
            "$nomention\n$if[$authorID==$botOwnerID]\n$sendMessage[¡Tú eres el desarrollador de este bot!]\n$else\n$sendMessage[¡Tú no eres el desarrollador de este bot!]\n$endif"
        ],
        "images_example":
        [f"{api}/funcion/images/else.png"],
        "deprecated":
        False
    },
    "elseif": {
        "name":
        "$elseif[]",
        "tag":
        "$elseif[Condicion]",
        "description":
        "Comprueba la condición proporcionada solo si las condiciones anteriores `$if[]` o `$elseif[]` devolvieron falso. Si la condición proporcionada es verdadera, se ejecutará el siguiente bloque de código.\n🧙‍♂️ ¡Solo para BDScript 2!",
        "example": [
            "$nomention\n$if[$authorID==$botOwnerID]\n$sendMessage[Desarrollador]\n$elseif[$authorID==$serverOwner]\n$sendMessage[Propietario del servidor]\n$endif"
        ],
        "images_example": [""],
        "deprecated":
        False
    },
    "embeddedURL": {
        "name":
        "$embeddedURL[]",
        "tag":
        "$embeddedURL[URL;(Indice)]",
        "description":
        "Establece el título como un hipervínculo.",
        "example": [
            "$nomention\n$title[Diseñador de bots para Discord]\n$embeddedURL[https://botdesignerdiscord.com]\n$description[¡Hola mundo!]\n$color[#683cb4]"
        ],
        "images_example": [
            f"{api}/funcion/images/embeddedURL.png"
        ],
        "deprecated":
        False
    },
    "$embedSuppressErrors": {
        "name":
        "$embedSuppressErrors",
        "tag":
        "$embedSuppressErrors[]",
        "description":
        "Suprime los mensajes de error, responde con el embed si hay algún error.",
        "example": [
            "$nomention\n$embedSuppressErrors[¡Error!;❌¡Expresión matemática no válida!;#ff0000;;Calculadora]\nResultado:\n**$calcular[$mensaje]**"
        ],
        "images_example": [
            f"{api}/funcion/images/embedSuppressErrors.png"
        ],
        "deprecated":
        False
    },
    "emoteCount": {
        "name":
        "$emoteCount",
        "tag":
        "$emoteCount",
        "description":
        "Devuelve el número de emojis en el servidor actual.",
        "example":
        ["$nomention\n¡Hay emojis de $emoteCount en $serverName[$guildID]!"],
        "images_example": [
            f"{api}/funcion/images/emoteCount.png"
        ],
        "deprecated":
        False
    },
    "enabled": {
        "name":
        "$enabled[]",
        "tag":
        "$enabled[Habilitado; Mensaje de error]",
        "description":
        "Le permite habilitar/deshabilitar comandos.",
        "example": [
            "$nomention\n$c[El valor de la variables es \"true\"]\n$enabled[$getServerVar[enabled];❌ ¡Este comando está deshabilitado!]"
        ],
        "images_example": [
            f"{api}/funcion/images/enable-1.png",
            f"{api}/funcion/images/enable-2.png"
        ],
        "deprecated":
        False
    },
    "enableDecimals": {
        "name":
        "$enableDecimals[]",
        "tag":
        "$enableDecimals[Habilitar?]",
        "description":
        "Activa/desactiva los decimales en funciones matemáticas.",
        "example": [
            "$nomention\n$c[Con la funcion]\n$enableDecimals[yes]\n$divide[1;5]",
            "$nomention\n$c[Sin la funcion]\n$divide[1;5]"
        ],
        "images_example": [
            f"{api}/funcion/images/enableDecimals-1.png",
            f"{api}/funcion/images/enableDecimals-2.png"
        ],
        "deprecated":
        False
    },
    "endif": {
        "name":
        "$endif",
        "tag":
        "$endif",
        "description":
        "Finaliza una declaración if.",
        "example":
        ["$nomention\n$if[$message==BDFD]\$sendMessage[Amo BDFD!]\n$endif"],
        "images_example":
        [f"{api}/funcion/images/endif.png"],
        "deprecated":
        False
    },
    "ephemeral": {
        "name":
        "$ephemeral",
        "tag":
        "$ephemeral",
        "description":
        "Hace que la respuesta del bot sea efímera.",
        "example": ["$nomention\n$ephemeral\n¡Hola!"],
        "images_example": [
            f"{api}/funcion/images/ephemeral.png"
        ],
        "deprecated":
        False
    },
    "eval": {
        "name":
        "$eval[]",
        "tag":
        "$eval[Codigo de funte BDScript]",
        "description":
        "Evalúa el código BDScript proporcionado.",
        "example": [
            "$nomention\n$onlyForIDs[$botOwnerID;❌ ¡Solo el propietario del bot puede usarlo!]\n$eval[$message]"
        ],
        "images_example":
        [f"{api}/funcion/images/eval.png"],
        "deprecated":
        False
    },
    "executionTime": {
        "name":
        "$executionTime",
        "tag":
        "$executionTime",
        "description":
        "Devuelve cuánto tiempo tardó en ejecutarse el comando, en milisegundos.",
        "example": ["$nomention\nPong!\n$executionTime ms"],
        "images_example": [
            f"{api}/funcion/images/executionTime.png"
        ],
        "deprecated":
        False
    },
    "findChannel": {
        "name":
        "$findChannel[]",
        "tag":
        "$findChannel[Canal]",
        "description":
        "Encuentra la ID de un canal a partir del nombre, ID o mención del canal dado.",
        "example": ["$nomention\nID del canal: $findChannel[$message]"],
        "images_example": [
            f"{api}/funcion/images/findChannel.png"
        ],
        "deprecated":
        False
    },
    "findRole": {
        "name":
        "$findRole[]",
        "tag":
        "$findRole[Rol]",
        "description":
        "Encuentra la ID de un rol a partir del nombre, ID o mención del rol dado.",
        "example": ["$nomention\nID del rol: $findRole[$message]"],
        "images_example": [
            f"{api}/funcion/images/findRole.png"
        ],
        "deprecated":
        False
    },
    "findUser": {
        "name":
        "$findUser[]",
        "tag":
        "$findUser[Usuario;(¿Devolver ID de autor?)]",
        "description":
        "Encuentra la ID de un usuario a partir del nombre, ID o mención del usuario dado.",
        "example": ["$nomention\nID del usuario: $findUser[$message]"],
        "images_example": [
            f"{api}/funcion/images/findUser.png"
        ],
        "deprecated":
        False
    },
    "footer": {
        "name":
        "$footer",
        "tag":
        "$footer[Texto;(Indice)]",
        "description":
        "Establece el texto del pie de página para insertar a la inserrcion o embed.",
        "example": ["$nomention\n$footer[¡Hola! Soy un pie de página.]"],
        "images_example": [
            f"{api}/funcion/images/footer.png"
        ],
        "deprecated":
        False
    },
    "footerIcon": {
        "name":
        "$footerIcon[]",
        "tag":
        "$footerIcon[URL]",
        "description":
        "Establece el icono de pie de página para insertar a la inserrcion o embed.",
        "example": [
            "$nomention\n$footer[⬅️ ¡Ese es un icono de pie de página!]\n$footerIcon[$authorAvatar]"
        ],
        "images_example": [
            f"{api}/funcion/images/footerIcon.png"
        ],
        "deprecated":
        False
    },
    "getBanReason": {
        "name":
        "$getBanReason[]",
        "tag":
        "$getBanReason[ID de usuario;(ID de gremio)]",
        "description":
        "Obtiene el motivo de la prohibición del usuario.",
        "example":
        ["$nomention\nMotivo del baneo: $getBanReason[$mentioned[1;false]]"],
        "images_example": [
            f"{api}/funcion/images/getBanReason.png"
        ],
        "deprecated":
        False
    },
    "getBotInvite": {
        "name":
        "$getBotInvite",
        "tag":
        "$getBotInvite",
        "description":
        "Devuelve la URL de invitación del bot.",
        "example": ["$nometion\n¡Invitame! $getBotInvite"],
        "images_example": [
            f"{api}/funcion/images/getBotInvite.png"
        ],
        "deprecated":
        False
    },
    "getChannelVar": {
        "name":
        "$getChannelVar",
        "tag":
        "$getChannelVar[Nombre de la variable;(ID del canal)]",
        "description":
        "Devuelve el valor de la variable de canal proporcionada.",
        "example": [
            "$nomention\nEl comando se usó `$getChannelVar[Usos]` veces en este canal"
        ],
        "images_example": [
            f"{api}/funcion/images/getBotInvite.png"
        ],
        "deprecated":
        False
    },
    "getCooldown": {
        "name":
        "$getCooldown[]",
        "tag":
        "$getCooldown[tipo de enfriamiento (normal/servidor/global)]",
        "description":
        "Devuelve cuánto tiempo queda en el tiempo de reutilización, en segundos.",
        "example": [
            "$nomention\n$cooldown[1h;¡Estás en tiempo de espera! (<t:$sum[$getTimestamp;$getCooldown[normal]]>)]\n¡Hola Mundo!\n$c[Este ejemplo debe usarse únicamente en BDScript 2.]"
        ],
        "images_example": [
            f"{api}/funcion/images/getCooldown.png"
        ],
        "deprecated":
        False
    },
    "getCustomStatus": {
        "name":
        "$getCustomStatus[]",
        "tag":
        "$getCustomStatus[ID de usuario]",
        "description":
        "Devuelve el estado personalizado de un usuario.",
        "example":
        ["$nomention\nTu estado customizable: $getCustomStatus[$authorID]"],
        "images_example": [
            f"{api}/funcion/images/getCustomStatus.png"
        ],
        "deprecated":
        False
    },
    "getEmbedData": {
        "name":
        "getEmbedData[]",
        "tag":
        "$getEmbedData[ID de canal;ID de mensaje;Índice de inserción;Propiedad de inserción (título/descripción/pie de página/color/imagen/marca de tiempo)]",
        "description":
        "Obtiene datos incrustados del mensaje proporcionado.",
        "example": [
            "$nomention\nTitulo:\n$getEmbedData[$channelID;$message[1];1;title]\nDescripcion:\n$getEmbedData[$channelID;$message[1];1;description]\nPie de pagina:\n$getEmbedData[$channelID;$message[1];1;footer]"
        ],
        "images_example": [
            f"{api}/funcion/images/getEmbedData.png"
        ],
        "deprecated":
        False
    },
    "getInviteInfo": {
        "name":
        "$getInviteInfo[]",
        "tag":
        "$getInviteInfo[Código de invitación;Propiedad de invitación]",
        "description":
        "Devuelve información sobre el código de invitación proporcionado.",
        "example": [
            "$nomention\n$argsCheck[>1;¡Proporcione un código de invitación válido!]\n$title[Información de invitación]\n$description[Usos: $getInviteInfo[$mensaje;uses]\nCanal: $getInviteInfo[$message;channel]\nFecha:\n$getInviteInfo[$message;creationDate]\nInvitador: $getInviteInfo[$message;inviter]\nTemporal: $getInviteInfo[$message;isTemporary]]\n$color[#673ab7]"
        ],
        "images_example": [
            f"{api}/funcion/images/getEmbedData.png"
        ],
        "deprecated":
        False
    },
    "getLeaderboardValue": {
        "name":
        "$getLeaderboardValue[]",
        "tag":
        "$getLeaderboardValue[Tipo de variable;Nombre de variable;Tipo de clasificación;Posición;(Tipo de retorno)]",
        "description":
        "Obtiene un valor de tabla de clasificación.",
        "example": [
            "$nomention\n$title[**Líder mundial**]\n$description[#1 - $getLeaderboardValue[globalUser;Dinero;asc;1]\n#2 - $getLeaderboardValue[globalUser;Dinero;asc;2]\n#3 - $getLeaderboardValue[globalUser;Dinero;asc;3]\n#4 - $getLeaderboardValue[globalUser;Dinero;asc;4]\n#5 - $getLeaderboardValue[globalUser;Dinero;asc;5]\n#6 - $getLeaderboardValue[globalUser;Dinero;asc;6]\n#7 - $getLeaderboardValue[globalUser;Dinero;asc;7]\n#8 - $getLeaderboardValue[globalUser;Dinero;asc;8]\n#9 - $getLeaderboardValue[globalUser;Dinero;asc;9]\n#10 - $getLeaderboardValue[globalUser;Money;asc;10]]\n$color[FFFF00]\n$c[Esto es para variables de usuario global.]"
        ],
        "images_example": [
            f"{api}/funcion/images/getLeaderboardValue.png"
        ],
        "deprecated":
        False
    },
    "getMessage": {
        "name":
        "$getMessage[]",
        "tag":
        "$getMessage[ID de canal; ID de mensaje; (Propiedad)]",
        "description":
        "Obtiene datos del mensaje proporcionado.",
        "example": [
            "$nomention\n$argsCheck[>2;¡Proporcione un canal y un ID de mensaje! Uso: `!quote (canal) (ID de mensaje)`]\n$description[$getMessage[$findChannel[$message[1]];$message[2]]]\n$color[#673ab7]\n$authorIcon[$getMessage[$findChannel[$message[1]];$message[2];avatar]]\n$autgor[$getMessage[$findChannel[$message[1]];$message[2];nombre de usuario]#$discriminator[$getMessage[$findChannel[$message[1]];$message[2];authorID]] ]"
        ],
        "images_example": [
            f"{api}/funcion/images/getMessage.png"
        ],
        "deprecated":
        False
    },
    "getReactions": {
        "name":
        "$getReactions[]",
        "tag":
        "$getReactions[ID de canal;ID de mensaje;Separador;Emoji]",
        "description":
        "Devuelve una lista de usuarios que reaccionaron a un mensaje.",
        "example": ["$nomention\n$getReactions[$channelID;$message[1];, ;✅]"],
        "images_example": [
            f"{api}/funcion/images/getReactions.png"
        ],
        "deprecated":
        False
    },
    "getRoleColor": {
        "name":
        "$getRoleColor[]",
        "tag":
        "$getRoleColor[ID Rol]",
        "description":
        "Devuelve el color hexadecimal de color de un rol.",
        "example": [
            "$nomention\n$description[<@$authorID>'s color: #$getRoleColor[$highestRole[$authorID]]]\n$color[$getRoleColor[$highestRole[$authorID]]]"
        ],
        "images_example": [
            f"{api}/funcion/images/getRoleColor.png"
        ],
        "deprecated":
        False
    },
    "getServerInvite": {
        "name":
        "$getServerInvite[], $getServerInvite",
        "tag":
        "$getServerInvite[ID servidor]",
        "description":
        "Devuelve la URL de invitación del servidor actual.",
        "example": ["$nomention\Link: $getServerInvite"],
        "images_example": [
            f"{api}/funcion/images/getServerInvite.png"
        ],
        "deprecated":
        False
    },
    "getServerVar": {
        "name":
        "$getServerVar[]",
        "tag":
        "$getServerVar[Nombre de la variable;(ID del gremio)]",
        "description":
        "Devuelve el valor de la variable del servidor proporcionada.",
        "example":
        ["El servidor tiene `$getServerVar[galleta;$guildID]` de galletas."],
        "images_example": [
            f"{api}/funcion/images/getServerVar.png"
        ],
        "deprecated":
        False
    },
    "getTextSplitIndex": {
        "name":
        "$getTextSplitIndex[]",
        "tag":
        "$getTextSplitIndex[Valor]",
        "description":
        "Recupera el índice del valor proporcionado en `$textSplit[]`. Devuelve `-1` si no pudo encontrar el valor.",
        "example": [
            "$nomention\n$textSplit[Pastel-Pan;-]\n$getTextSplitIndex[$message[1]]"
        ],
        "images_example": [
            f"{api}/funcion/images/getTextSplitIndex.png"
        ],
        "deprecated":
        False
    },
    "getTextSplitLength": {
        "name":
        "$getTextSplitLength",
        "tag":
        "$getTextSplitLength",
        "description":
        "Devuelve el número de divisiones en `$textSplit[]`.",
        "example": [
            "$nomention\n$textSplit[Hola | Hola | Ey; | ]\n¡El texto se ha dividido en $getTextSplitLength elementos!"
        ],
        "images_example": [
            f"{api}/funcion/images/getTextSplitLength.png"
        ],
        "deprecated":
        False
    },
    "getTimestamp": {
        "name":
        "$getTimestamp[], $getTimestamp",
        "tag":
        "$getTimestamp[Unidad de tiempo]",
        "description":
        "Devuelve la marca de tiempo actual de [Unix](https://www.unixtimestamp.com) en la unidad de tiempo seleccionada.",
        "example": ["El timpo unix actual es: $getTimestamp"],
        "images_example": [
            f"{api}/funcion/images/getTimestamp.png"
        ],
        "deprecated":
        False
    },
    "getUserStatus": {
        "name":
        "$getUserStatus[]",
        "tag":
        "$getUserStatus[ID Usuario]",
        "description":
        "Devuelve el estado/presencia del usuario proporcionado.",
        "example": [
            "$nomention\nEl estado de $nickname[$mentioned[1;true]] es: $getUserStatus[$mentioned[1;true]]"
        ],
        "images_example": [
            f"{api}/funcion/images/getUserStatus.png"
        ],
        "deprecated":
        False
    },
    "getUserVar": {
        "name":
        "$getUserVar[]",
        "tag":
        "$getUserVar[Nombre de variable;(ID de usuario;ID de gremio)]",
        "description":
        "Devuelve un valor de variable de usuario local.",
        "example": [
            "$nomention\n<@$mentioned[1;true]> Tiene de monedas $getUserVar[Dinero;$mentioned[1;true]]."
        ],
        "images_example": [
            f"{api}/funcion/images/getUserVar.png"
        ],
        "deprecated":
        False
    },
    "getVar": {
        "name":
        "$getVar[]",
        "tag":
        "$getVar[Nombre de variable;(ID de usuario)]",
        "description":
        "Obtiene el valor de una variable global/de usuario global.",
        "example":
        ["$nomention\n¡Tienes monedas $getVar[Dinero;$mentioned[1;true]]!"],
        "images_example": [
            f"{api}/funcion/images/getVar.png"
        ],
        "deprecated":
        False
    },
    "giveRole": {
        "name":
        "$giveRole[]",
        "tag":
        "$giveRole[Usuario ID/Rol ID;(Role ID)]]",
        "description":
        "Agrega un rol a la usuario proporcionada.",
        "example": [
            "$nomention\n$onlyPerms[manageroles;¡Permisos faltantes!]\n\n$giveRole[$mentioned[1];$message[2]]\n¡Se agregó el rol **$roleName[$message[2]]** a **$username[$mentioned[1]]**!"
        ],
        "images_example": [
            f"{api}/funcion/images/giveRole.png"
        ],
        "deprecated":
        True
    },
    "globalCooldown": {
        "name":
        "$globalCooldown[]",
        "tag":
        "$globalCooldown[Duración;Mensaje de error]",
        "description":
        "Aplica un tiempo de reutilización al comando, el usuario no puede ejecutar el comando en ningún servidor hasta que finalice la \"Duración\". (A diferencia de `$cooldown`, que solo aplica el tiempo de reutilización al usuario en el servidor actual)",
        "example": [
            "$nomention\n$globalCooldown[30s;$username, ¡Estás en cooldown por %time%!]\nHola $username"
        ],
        "images_example": [
            f"{api}/funcion/images/globalCooldown.png"
        ],
        "deprecated":
        False
    },
    "globalUserLeaderboard": {
        "name":
        "$globalUserLeaderboard[]",
        "tag":
        "$globalUserLeaderboard[Nombre de variable;Tipo de ordenación (asc/desc)]",
        "description":
        "Devuelve el nombre de usuario y el valor de los diez primeros usuarios para la variable de usuario global dada.",
        "example": ["$nomention\n$globalUserLeaderboard[Dinero;desc]"],
        "images_example": [
            f"{api}/funcion/images/globalUserLeaderboard.png"
        ],
        "deprecated":
        False
    },
    "guildExists": {
        "name":
        "$guildExists[]",
        "tag":
        "$guildExists[ID servidor",
        "description":
        "Comprueba si el gremio/servidor proporcionado existe.",
        "example": ["$nomention\n$guildExists[$message[1]]"],
        "images_example": [
            f"{api}/funcion/images/globalUserLeaderboard.png"
        ],
        "deprecated":
        False
    },
    "guildID": {
        "name":
        "$guildID[], $guildID",
        "tag":
        "$guildID[Nombre del servidor]",
        "description":
        "Encuentra una ID de servidor utilizando el nombre de un servidor o si no se habre su corchetes devuelve ID del servidor donde se ejecuta el comando.",
        "example": ["$nomention\El ID del servidor es:\n$guildID[$message]"],
        "images_example": [
            f"{api}/funcion/images/guildID.png"
        ],
        "deprecated":
        False
    },
    "hasRole": {
        "name":
        "$hasRole[]",
        "tag":
        "$hasRole[Usuario ID;Rol ID]",
        "description":
        "Devuelve true/false, si una usuario tiene o no el rol proporcionado.",
        "example": ["$nomention\n$hasRole[$authorID;$mentionedRole[1]]"],
        "images_example": [
            f"{api}/funcion/images/hasRole.png"
        ],
        "deprecated":
        False
    },
    "highestRole": {
        "name":
        "$highestRole[], $highestRole",
        "tag":
        "$highestRole[Rol ID]",
        "description":
        "Devuelve el ID del rol más alto del usuario proporcionado (según su posición), si no se habre sus corchetes devuelve el ID del rol mas alto del autor.",
        "example": [
            "$nomention\nRol más alto de $username[$mentioned[1;true]]:\n$roleName[$highestRole[$mentioned[1;yes]]] ($highestRole[$mentioned[1;yes]])"
        ],
        "images_example": [
            f"{api}/funcion/images/highestRole.png"
        ],
        "deprecated":
        False
    },
    "highestRoleWithPerms": {
        "name":
        "$highestRoleWithPerms[]",
        "tag":
        "$highestRoleWithPerms[Permisos]",
        "description":
        "Devuelve el rol más alto en el servidor actual que tiene todos los permisos proporcionados.",
        "example": [
            "$nomention\nRol más alto con administrador: $roleName[$highestRoleWithPerms[admin]]\n($highestRoleWithPerms[admin])"
        ],
        "images_example": [
            f"{api}/funcion/images/highestRoleWithPerms.png"
        ],
        "deprecated":
        False
    },
    "hostingExpireTime": {
        "name":
        "$hostingExpireTime[], $hostingExpireTime",
        "tag":
        "$hostingExpireTime[¿Devolver marca de tiempo de Unix?]",
        "description":
        "Devuelve la fecha de vencimiento del alojamiento de su bot. Si se proporciona \"true\", la función devuelve la fecha de vencimiento en una marca de tiempo UNIX. Esto solo es valido si se habre sus corchetes.",
        "example": ["Estaré desconectado <t:$hostingExpireTime[true]:R>"],
        "images_example": [
            f"{api}/funcion/images/hostingExpireTime.png"
        ],
        "deprecated":
        False
    },
    "hour": {
        "name":
        "$hour",
        "tag":
        "$hour",
        "description":
        "Devuelve la hora actual.",
        "example": ["$nomention\nHora actual: $hora"],
        "images_example": [
            f"{api}/funcion/images/hostingExpireTime.png"
        ],
        "deprecated":
        False
    },
    "hypesquad": {
        "name":
        "$hypesquad[]",
        "tag":
        "$hypesquad[ID usuario]",
        "description":
        "Devuelve el nombre de la casa hypesquad del usuario proporcionado.",
        "example": ["$nomention\nEstás en la casa: $hypesquad[$authorID]."],
        "images_example": [
            f"{api}/funcion/images/hypesquad.png"
        ],
        "deprecated":
        False
    },
    "if": {
        "name":
        "$if[]",
        "tag":
        "$if[Condicion]",
        "description":
        "Ejecuta el siguiente bloque de código si la condición proporcionada es verdadera.",
        "example": [
            "$nomention\n$if[$authorID==$serverOwner]\n$sendMessage[¡Tú eres el dueño de este servidor!]\n$endif"
        ],
        "images_example":
        [f"{api}/funcion/images/if.png"],
        "deprecated":
        False
    },
    "ignoreChannels": {
        "name":
        "$ignoreChannels",
        "tag":
        "$ignoreChannels[ID de canal;...;Mensaje de error]",
        "description":
        "El comando no se puede ejecutar en ninguno de los canales proporcionados. Si se ignora el canal, se devuelve el \"mensaje de error\" proporcionado.",
        "example": [
            "$nomention\n$ignoreChannels[1099033713687404614;❌ ¡Ese comando no se puede usar en este canal!]\n\nHola $username"
        ],
        "images_example": [
            f"{api}/funcion/images/ignoreChannels.png"
        ],
        "deprecated":
        False
    },
    "ignoreLinks": {
        "name":
        "$ignoreLinks",
        "tag":
        "$ignoreLinks",
        "description":
        "",
        "example": [
            "$nomention\n$ignoreLinks\nAquí hay una tostadora URL:\nhttps://media.discordapp.net/attachments/1011682358031826994/1027580044928888832/856506821023629332.png"
        ],
        "images_example": [
            f"{api}/funcion/images/ignoreLinks.png"
        ],
        "deprecated":
        False
    },
    "image": {
        "name":
        "$image[]",
        "tag":
        "$image[URL;(Indice)]",
        "description":
        "Agrega una imagen a la inserción.",
        "example": ["$nomention\n$image[$userAvatar[$botID]]"],
        "images_example":
        [f"{api}/funcion/images/image.png"],
        "deprecated":
        False
    },
    "input": {
        "name":
        "$input[]",
        "tag":
        "$input[ID de entrada de texto]",
        "description":
        "Recupera la entrada de un modal.",
        "example": [
            "$nometion\nNombre: $input[modalInput1]\nPronombres: $input[modalInput2]\nAcerca de mí: $input[modalInput3]"
        ],
        "images_example":
        [f"{api}/funcion/images/input.png"],
        "deprecated":
        False
    },
    "isAdmin": {
        "name":
        "$isAdmin[]",
        "tag":
        "$isAdmin[ID Usuario]",
        "description":
        "Devuelve si el usuario proporcionado tiene permiso de administrador o no.",
        "example":
        ["$nomention\n¿Es usted administrador?: `$isAdmin[$authorID]`"],
        "images_example": [
            f"{api}/funcion/images/isAdmin.png"
        ],
        "deprecated":
        False
    },
    "isBanned": {
        "name":
        "$isBanned[]",
        "tag":
        "$isBanned[ID Usuario]",
        "description":
        "Devuelve si un usuario está prohibido en el servidor actual o no. Requiere el permiso BAN_MEMBERS.",
        "example": ["$nomention\nEsta baneado?: $isBanned[$mentioned[1]]"],
        "images_example": [
            f"{api}/funcion/images/isBaned.png"
        ],
        "deprecated":
        False
    },
    "isBoolean": {
        "name":
        "$isBoolean[]",
        "tag":
        "$isBoolean[Texto]",
        "description":
        "Devuelve si el texto proporcionado es booleano o no.",
        "example": ["$nomention\n$isBolean[$message]"],
        "images_example": [
            f"{api}/funcion/images/isBoolean.png"
        ],
        "deprecated":
        False
    },
    "isBot": {
        "name":
        "$isBot[]",
        "tag":
        "$isBot[ID usuario]",
        "description":
        "",
        "example": ["$nomention\n¿Bot? $isBot[$findUser[$message];true]"],
        "images_example":
        [f"{api}/funcion/images/isBot.png"],
        "deprecated":
        False
    },
    "isHoisted": {
        "name":
        "$isHoisted[]",
        "tag":
        "$isHoisted[ID rol]",
        "description":
        "Devuelve si un rol se muestra por separado o no.",
        "example": ["$nomention\n$isHoisted[$findRole[$message]]"],
        "images_example": [
            f"{api}/funcion/images/isHoisted.png"
        ],
        "deprecated":
        False
    },
    "isMentionable": {
        "name":
        "$isMentionable[]",
        "tag":
        "$isMentionable[ID Usuario]",
        "description":
        "Devuelve si un rol es mencionado por todas o no.",
        "example": ["$nomention\n$isMentionable[$findRole[$messge]]"],
        "images_example": [
            f"{api}/funcion/images/isMentionable.png"
        ],
        "deprecated":
        False
    },
    "isNSFW": {
        "name":
        "$isNSFW[]",
        "tag":
        "$isNSFW[Canal ID]",
        "description":
        "Devuelve si el canal proporcionado es NSFW (no seguro para el trabajo) o no.",
        "example":
        ["$nomention\n¿Es <#$channelID> NSFW?: `$isNSFW[$channelID]"],
        "images_example": [
            f"{api}/funcion/images/isNSFW.png"
        ],
        "deprecated":
        False
    },
    "isNumber": {
        "name":
        "$isNumber[]",
        "tag":
        "$isNumber[Valor]",
        "description":
        "Devuelve si el valor proporcionado es un número o no.",
        "example": ["$nomention\nEs un numero?: $isNumber[$message]"],
        "images_example": [
            f"{api}/funcion/images/isNumber.png"
        ],
        "deprecated":
        False
    },
    "isSlash": {
        "name":
        "$isSlash",
        "tag":
        "$isSlash",
        "description":
        "Devuelve si el comando se ejecutó como un comando de barra diagonal(slash) o no.",
        "example": ["$nomention\nEste codigo se uso en slash?: $isSlash"],
        "images_example": [
            f"{api}/funcion/images/isSlash.png"
        ],
        "deprecated":
        False
    },
    "isTicket": {
        "name":
        "$isTicket[]",
        "tag":
        "$isTicket[Canal ID]",
        "description":
        "Comprueba si el canal actual o especificado es un ticket o no.",
        "example": [
            "$nomention\n$onlyIf[$isTicket[]==true;¡Este comando solo se puede usar en un ticket!]\n¡Esto es un ticket!"
        ],
        "images_example": [
            f"{api}/funcion/images/isTicket.png"
        ],
        "deprecated":
        False
    },
    "isTimedOut": {
        "name":
        "$isTimedOut[]",
        "tag":
        "$isTimedOut[Usuario]",
        "description":
        "Comprueba si el tiempo de espera del usuario especificado ha expirado o no.",
        "example":
        ["$nomention\nEsta muteado el usuario?: $isTimedOut[$mentioned[1]]"],
        "images_example": [
            f"{api}/funcion/images/isTimeOut.png"
        ],
        "deprecated":
        False
    },
    "isUserDMEnabled": {
        "name":
        "$isUserDMEnabled[]",
        "tag":
        "$isUserDMEnabled[Usuario ID]",
        "description":
        "Comprueba si el bot puede mandar un DM la usuaria o no.",
        "example": [
            "$nomention\n$onlyIf[$isUserDMEnabled[$authorID]==true;❌ No se pudo enviarte un mensaje de texto. ¡Asegúrate de tener tus DM activados!]\n$dm\n$message"
        ],
        "images_example": [
            f"{api}/funcion/images/isUserDMEnabled.png"
        ],
        "deprecated":
        False
    },
    "isValidHex": {
        "name":
        "$isValidHex[]",
        "tag":
        "$isValidHex[Colo hexadecimal]",
        "description":
        "Comprueba si el color hexadecimal dado es válido o no.",
        "example": ["$nomention\n$isValidHex[$message[1]]"],
        "images_example": [
            f"{api}/funcion/images/isValidHex.png"
        ],
        "deprecated":
        False
    },
    "joinSplitText": {
        "name":
        "$joinSplitText[]",
        "tag":
        "$joinSplitText[Separador]",
        "description":
        "Une los valores de `$textSplit[]` con un separador proporcionado.",
        "example":
        ["$nomention\n$textSplit[Hola-ho-hey;-]\n$joinSplitText[\n]"],
        "images_example": [
            f"{api}/funcion/images/joinSplitText.png"
        ],
        "deprecated":
        False
    },
    "kick": {
        "name":
        "$kick[], $kick",
        "tag":
        "$kick[ID de usuario;(motivo)]",
        "description":
        "Expulsa a la usuaria proporcionada, solo si se habre los corchetes.",
        "example": [
            "$nomention\n$onlyPerms[kick;❌ ¡Necesitas el permiso `kick` para usarlo!]\n$argsCheck[>1;❌ Proporcione un usuario para patear. Uso: `!kick (usuario) <motivo>`.]\n$kick[$mentioned[1];$noMentionMessage]\n✅ Expulsado `$username[$mentioned[1]]#$discriminador[$mentioned[1]]`"
        ],
        "images_example":
        [f"{api}/funcion/images/kick.png"],
        "deprecated":
        False
    },
    "kickMention": {
        "name":
        "$kickMention[]",
        "tag":
        "$kickMention[Razon]",
        "description":
        "Una versión simplificada de `$kick`. Patea al usuario mencionado.",
        "example": [
            "$nomention\n$kickMention[$noMentionMessage]\n✅ ¡Expulsado `$username[$mentioned[1]]#$discriminador[$mentioned[1]]`!"
        ],
        "images_example": [
            f"{api}/funcion/images/kickMention.png"
        ],
        "deprecated":
        False
    },
    "lowestRole": {
        "name":
        "$lowestRole[], $lowestRole",
        "tag":
        "$lowestRole[Usuario ID]",
        "description":
        "Devuelve el ID del rol más bajo del servidor actual (según su posición). solo si no se habre sus corchetes, si es asi se debe proporcionar el ID de un usuario.",
        "example": [
            "$nomention\nEl rol más bajo del servidor: <@&$lowestRole> ($lowestRole)",
            "$nomention\n$username[$mentioned[1;yes]]'s Rol mas bajo:\n$roleName[$lowestRole[$mentioned[1;yes]]] qAwq  ($lowestRole[$mentioned[1;yes]])"
        ],
        "images_example": [
            f"{api}/funcion/images/lowestRole.png"
        ],
        "deprecated":
        False
    },
    "lowestRoleWithPerms": {
        "name":
        "$lowestRoleWithPerms[]",
        "tag":
        "$lowestRoleWithPerms[Permisos;...]",
        "description":
        "Devuelve el rol más bajo en el servidor que tiene todos los permisos proporcionados.",
        "example": [
            "$nomention\nRol más bajo con administrador: $roleName[$lowestRoleWithPerms[admin]] ($lowestRoleWithPerms[admin])"
        ],
        "images_example": [
            f"{api}/funcion/images/lowestRoleWithPerms.png"
        ],
        "deprecated":
        False
    },
    "max": {
        "name":
        "$max[]",
        "tag":
        "$max[A;B]",
        "description":
        "Devuelve el número más grande de los números proporcionados.",
        "example": ["$nomention\n$max[100;20;50]"],
        "images_example":
        [f"{api}/funcion/images/max.png"],
        "deprecated":
        False
    },
    "membersCount": {
        "name":
        "$membersCount[], $membersCount",
        "tag":
        "$membersCount[Presencia]",
        "description":
        "Devuelve la cantidad de miembros del gremio actual con presencia proporcionada, solo si se habre los corchetes de la funcion.",
        "example": [
            "$nomention\nhay $membersCount[online] usuarios en línea en este servidor"
        ],
        "images_example": [
            f"{api}/funcion/images/membersCount.png"
        ],
        "deprecated":
        False
    },
    "mentioned": {
        "name":
        "$mentioned[]",
        "tag":
        "$mentioned[Numero mencion;(Retornar author?)]",
        "description":
        "Devuelve el ID de la usuario mencionada.",
        "example": ["$nomention\n$mentioned[1;false]"],
        "images_example": [
            f"{api}/funcion/images/mentioned.png"
        ],
        "deprecated":
        False
    },
    "mentionedChannels": {
        "name":
        "$mentionedChannels[]",
        "tag":
        "$mentionedChannels[Numero mencion;(¿Retorno de corriente?)]",
        "description":
        "Devuelve el ID del canal mencionado.",
        "example": ["$nomention\n$mentionedChannels[1]"],
        "images_example": [
            f"{api}/funcion/images/mentionedChannels.png"
        ],
        "deprecated":
        False
    },
    "mentionedRoles": {
        "name":
        "$mentionedRoles[]",
        "tag":
        "$mentionedRoles[Numero mencion]",
        "description":
        "Devuelve el ID del rol mencionado.",
        "example": ["$nomention\n<@&$mentionedRoles[1]>"],
        "images_example": [
            f"{api}/funcion/images/mentionedRoles.png"
        ],
        "deprecated":
        False
    },
    "message": {
        "name":
        "$message[], $message",
        "tag":
        "",
        "description":
        "Devuelve un argumento del mensaje o la entrada de una opción de comando de barra diagonal, esto solo es valido si se abre sus corchetes.",
        "example":
        ["$if[$isSlash]==false]\n$message\n$else\n$message[decir]\n$endif"],
        "images_example": [""],
        "deprecated":
        False
    },
    "messageID": {
        "name":
        "$messageID",
        "tag":
        "$messageID",
        "description":
        "Devuelve el ID del mensaje del autor.",
        "example": ["$nomention\nMensaje ID: $messageID"],
        "images_example": [
            f"{api}/funcion/images/messageID.png"
        ],
        "deprecated":
        False
    },
    "min": {
        "name":
        "$min[]",
        "tag":
        "$min[A;B;...]",
        "description":
        "Devuelve el número más pequeño de los números proporcionados.",
        "example": ["$nomention\n$min[1;8;5]"],
        "images_example":
        [f"{api}/funcion/images/min.png"],
        "deprecated":
        False
    },
    "minute": {
        "name":
        "$minute",
        "tag":
        "$minute",
        "description":
        "Devuelve el minuto actual de esta hora.",
        "example": ["$nomention\nEl minuto es $minute"],
        "images_example": [
            f"{api}/funcion/images/minute.png"
        ],
        "deprecated":
        False
    },
    "modifyChannel": {
        "name":
        "$modifyChannel[]",
        "tag":
        "$modifyChannel[ID de canal;(nombre de canal;tema;NSFW;posición;ID de categoría)]",
        "description":
        "Edita un canal con los datos proporcionados.",
        "example": [
            "$nomention\n$c[Para este ejemplo, cambiaremos el nombre del canal de \"general\" a \"chat-cool\". Además de cambiar el tema del canal a '¡Una charla tranquila!'.]\n$modifyChannel[$channelID[general];chat-cool;chat-cool;!unchanged;!unchanged]\n✅ Canal modificado exitosamente."
        ],
        "images_example": [
            f"{api}/funcion/images/modifyChannel.png"
        ],
        "deprecated":
        False
    },
    "modifyChannelPerms": {
        "name":
        "$modifyChannelPerms[]",
        "tag":
        "$modifyChannelPerms[ID de canal;Permisos;ID de usuario/rol]",
        "description":
        "Modifica los permisos de un canal.",
        "example": [
            "$nomention'n$onlyPerms[managechannels;❌ ¡Necesitas el permiso de Manage_channels para usarlo!]\n✅ ¡<#$mentionedChannels[1;true]> bloqueados exitosamente!\n$modifyChannelPerms[$canalesmencionados[1;yes];-sendmessages;$guildID]"
        ],
        "images_example": [
            f"{api}/funcion/images/modifyChannelsPerms.png"
        ],
        "deprecated":
        True
    },
    "modifyRole": {
        "name":
        "$modifyRole[]",
        "tag":
        "$modifyRole[ID de rol;(Nombre de rol;Color hexadecimal;¿Izado?;¿Mencionable?)]",
        "description":
        "Modifica un rol existente.",
        "example": [
            "$nomention\n$argsCheck[>2;❌ ¡Proporcione los argumentos necesarios! Uso: `!nombre-rol (rol) (nuevoNombreRol)`]\n$onlyPerms[manageroles;❌ ¡Te falta el permiso de gestionar_roles!]\n$modifyRole[$findRole[$message[1]];$replaceText[$message;$message[1];;1];!sin cambios;!sin cambios;!sin cambios]\n$description[✅ Se cambió el nombre del rol de <@&$findRole[$message[1]]>]"
        ],
        "images_example": [
            f"{api}/funcion/images/modifyRole.png"
        ],
        "deprecated":
        False
    },
    "modifyRolePerms": {
        "name":
        "$modifyRolePerms[]",
        "tag":
        "$modifyRolePerms[Rol ID;Permisos;...]",
        "description":
        "Modifica los permisos de un rol.",
        "example": [
            "$nomention\n$modifyRolesPerms[$mentionedRoles[1];admin]\nRol modificado para ser admin."
        ],
        "images_example": [
            f"{api}/funcion/images/modifyRolePerms.png"
        ],
        "deprecated":
        False
    },
    "modulo": {
        "name":
        "$modulo[]",
        "tag":
        "$modulo[A;B]",
        "description":
        "Devuelve el resto entre números.",
        "example": ["El residuo de la division es: $modulo[10;5]"],
        "images_example": [
            f"{api}/funcion/images/modulo.png"
        ],
        "deprecated":
        False
    },
    "month": {
        "name":
        "$month",
        "tag":
        "$month",
        "description":
        "Devuelve el mes actual de este año.",
        "example": ["$nomention\nMes actual: $month"],
        "images_example":
        [f"{api}/funcion/images/month.png"],
        "deprecated":
        False
    },
    "multi": {
        "name":
        "$multi[]",
        "tag":
        "$multi[Numero;...]",
        "description":
        "Multiplica los números proporcionados.",
        "example": [
            "$nomention\n$argsCheck[>2;❌ Uso no válido. Uso: `!multiplicar (número1) (número2)`]\n$multi[$mensaje[1];$mensaje[2]]"
        ],
        "images_example":
        [f"{api}/funcion/images/multi.png"],
        "deprecated":
        False
    },
    "mute": {
        "name":
        "$mute[]",
        "tag":
        "$mute[Nombre Rol]",
        "description":
        "Silencia al usuario mencionado.",
        "example": [
            "$nomention'n$onlyPerms[manageroles;❌ Te falta permiso: `MANAGE_ROLES`.]\n$mute[Silenciado]\n✅ ¡$username[$mentioned[1]]#$discriminator[$mentioned[1]] se silenció con éxito!"
        ],
        "images_example":
        [f"{api}/funcion/images/mute.png"],
        "deprecated":
        False
    },
    "newModal": {
        "name":
        "$newModal[]",
        "tag":
        "$newModal[ID Nombre;Nombre]",
        "description":
        "",
        "example": [
            "$nomention\n$newModal[modal;Biografía del usuario]\n$addTextInput[modalInput1;short;¿Cómo te llamas?;3;30;yes;;Mikołaj]\n$addTextInput[modalInput2;short;¿Cuáles son tus pronombres?;2;30;yes;;Él/Él]\n$addTextInput[modalInput3;paragraph;¿Puedes hablarnos de ti?;5;1000;no;;Soy desarrollador]"
        ],
        "images_example": [""],
        "deprecated":
        False
    },
    "newSelectMenu": {
        "name":
        "$newSelectMenu[]",
        "tag":
        "$newSelectMenu[ID de menú;Min;Max;(Marcador de posición;ID de mensaje)]",
        "description":
        "Agrega un menú de selección a un mensaje.",
        "example": [
            "$nomention\nun mensaje genial\n$newSelectMenu[Ejemplo;1;1;Elija alguna opción]\n$addSelectMenuOption[Ejemplo;Primero;primera opción;La primera opción]\n$addSelectMenuOption[Ejemplo;Segundo;segunda-opción;La segunda opción]\n$addSelectMenuOption[Ejemplo;Tercero;tercera-opción;La tercera opción]"
        ],
        "images_example": [
            f"{api}/funcion/images/newSelectMenu.png"
        ],
        "deprecated":
        False
    },
    "newTicket": {
        "name":
        "$newTicket[]",
        "tag":
        "$newTicket[ID de categoría/Nombre;Mensaje sin preguntas;En mensaje de ticket;Mensaje al usuario;Mensaje de error;(Número de ticket;ID de devolución del mensaje de ticket?)]",
        "description":
        "Crea un nuevo ticket.",
        "example": [
            "$nomention\n$newTicket[Tickets;No se proporcionó ningún asunto.;Gracias por crear un ticket. Explique su problema en detalle para que podamos ayudarlo.\nAsunto: {subject}\nUsuario: <@$authorID>;¡Ticket creado! {channel};¡No se pudo generar el boleto!]"
        ],
        "images_example": [
            f"{api}/funcion/images/ticket.png"
        ],
        "deprecated":
        False
    },
    "nickname": {
        "name":
        "$nickname[], $nickname",
        "tag":
        "",
        "description":
        "Devuelve el apodo de el usuario dada solo si se habre sus corchetes de lo contrario retorna el apodo del autor.",
        "example": [
            "$nomention\n$allowUserMentions[]\nEl apodo de <@$mentioned[1;true]> es `$nickname[$mentioned[1;true]]`"
        ],
        "images_example": ["$c[Este codigo no contiene $nomention]\nHola"],
        "deprecated":
        False
    },
    "nomention": {
        "name":
        "$nomention",
        "tag":
        "$nomention",
        "description":
        "Deshabilita la mención predeterminada del autor",
        "example": ["$c[Este codigo no tiene $nomention]\nHola"],
        "images_example": [
            f"{api}/funcion/images/nomention.png"
        ],
        "deprecated":
        False
    },
    "noMentionMessage": {
        "name":
        "$noMentionMessage[], $noMentionMessage",
        "tag":
        "",
        "description":
        "Devuelve el mensaje completo del usuario sin ninguna mención (sin el activador del comando). pero si se habre sus corchetes devuelve un argumento del mensaje del usuario omitiendo cualquier mención.",
        "example": [
            "$nomention\n1. $noMentionMessage[1]\n3. $noMentionMessage[3]\nMayor argumento: $noMentionMessage[>]"
        ],
        "images_example": [
            f"{api}/funcion/images/noMentionMessage.png"
        ],
        "deprecated":
        False
    },
    "nodeVersion": {
        "name":
        "$nodeVersion[], $nodeVersion",
        "tag":
        "",
        "description":
        "Devuelve la versión del nodo actual pero si se habre sus corchets devuelve la versión del nodo especificado.",
        "example": ["$nometion\nVersión de 13 nodo: `$nodeVersion[13]`"],
        "images_example": [
            f"{api}/funcion/images/nodeVersion.png"
        ],
        "deprecated":
        False
    },
    "numberSeparator": {
        "name":
        "$numberSeparator[]",
        "tag":
        "$numberSeparator[Numero;(Separador)]",
        "description":
        "Separa las miles en un número.",
        "example": ["$nomention\nNumeros separados: $numberSeparator[5000;,]"],
        "images_example": [
            f"{api}/funcion/images/numberSeparator.png"
        ],
        "deprecated":
        False
    },
    "onlyAdmin": {
        "name":
        "$onlyAdmin[]",
        "tag":
        "$onlyAdmin[Mensaje de error.]",
        "description":
        "Permite la ejecución de comandos solo para usuarios con permiso de administrador.",
        "example": [
            "$nomention\n$onlyAdmin[❌ ¡Solo los administradores pueden usar este comando!]\n\n$c[Ponga su código aquí.]"
        ],
        "images_example": [
            f"{api}/funcion/images/onlyAdmin.png"
        ],
        "deprecated":
        False
    },
    "onlyBotChannelPerms": {
        "name":
        "$onlyBotChannelPerms[]",
        "tag":
        "$onlyBotChannelPerms[Canal ID;Permisos;..;Mensaje de error]",
        "description":
        "El comando solo se puede ejecutar si el bot tiene todos los permisos proporcionados en un canal determinado.",
        "example": [
            "$nomention$onlyBotChannelPerms[$channelID;sendmessages;embedlinks;❌ ¡Faltan permisos!]\n$description[¡Oye tengo permis para enviar \"Enviar Enlaces\" en el canal actual]"
        ],
        "images_example": [
            f"{api}/funcion/images/onlyBotChannelPerms.png"
        ],
        "deprecated":
        False
    },
    "onlyBotPerms": {
        "name":
        "$onlyBotPerms[]",
        "tag":
        "$onlyBotPerms[Permisos;..;Mensaje de error]",
        "description":
        "$onlyBotPerms[Permisos;...;Mensaje de error]",
        "example": [
            "$nomention\n$onlyBotPerms[sendmessages;embedlinks;❌ ¡Faltan permisos!]\n$description[¡Oye! Tengo permiso para \"Incrustar enlaces\".]"
        ],
        "images_example": [
            f"{api}/funcion/images/onlyBotPerms.png"
        ],
        "deprecated":
        False
    },
    "onlyForCategories": {
        "name":
        "$onlyForCategories[]",
        "tag":
        "$onlyForCategories[ID categorias;...;Mensaje de rror]",
        "description":
        "El comando solo se puede ejecutar en las categorías proporcionadas.",
        "example": [
            "$nomention\n$onlyForCategories[790620501927526462;❌ ¡Este comando no se puede ejecutar en esta categoría!]\n\n$c[Ponga su código aquí.]"
        ],
        "images_example": [
            f"{api}/funcion/images/onlyForCategories.png"
        ],
        "deprecated":
        False
    },
    "onlyForChannels": {
        "name":
        "$onlyForChannels[]",
        "tag":
        "$onlyForChannels[Canal ID;...;Mensaje de error]",
        "description":
        "El comando solo se puede ejecutar en los canales proporcionados.",
        "example": [
            "$nomention\n$onlyForChannels[1050809741137412177;816767374610923601;❌ ¡Este comando no se puede ejecutar en este canal!]\n\n$c[Ponga su código aquí.]"
        ],
        "images_example": [
            f"{api}/funcion/images/onlyForChannels.png"
        ],
        "deprecated":
        False
    },
    "onlyForIDs": {
        "name":
        "$onlyForIDs[]",
        "tag":
        "$onlyForIDs[ID de usuario;...;Mensaje de error]",
        "description":
        "El comando solo puede ser ejecutado por los usuarios proporcionados.",
        "example": [
            "$nomention\n$onlyForIDs[980221602220363816;Solo mi creador puede usar esto]\nHola creador"
        ],
        "images_example": [
            f"{api}/funcion/images/onlyForIDs.png"
        ],
        "deprecated":
        False
    },
    "onlyForRoles": {
        "name":
        "$onlyForRoles[]",
        "tag":
        "$onlyForRoles[Nombres de roles;...;Mensaje de error]",
        "description":
        "El comando solo lo pueden ejecutar usuarios con cualquiera de los roles proporcionados.",
        "example": [
            "$nomention$onlyForRoles[Moderador;Admin;❌ ¡No tienes ninguno de los roles requeridos para usar este comando!]\n$c[Ponga su código aquí.]"
        ],
        "images_example": [
            f"{api}/funcion/images/onlyForRoles.png"
        ],
        "deprecated":
        False
    },
    "onlyForRolesIDs": {
        "name":
        "$onlyForRolesIDs[]",
        "tag":
        "$onlyForRoles[ID de roles;...;Mensaje de error]",
        "description":
        "El comando solo lo pueden ejecutar usuarios con cualquiera de los ID de los roles proporcionados.",
        "example": [
            "$nomention$onlyForRoles[1098761498232365157;❌ ¡No tienes ninguno de los roles requeridos para usar este comando!]\n$c[Ponga su código aquí.]"
        ],
        "images_example": [
            f"{api}/funcion/images/onlyForRolesIDs.png"
        ],
        "deprecated":
        False
    },
    "onlyForServers": {
        "name":
        "$onlyForServers[]",
        "tag":
        "$onlyForServers[ID servidor;...;Mensaje de error]",
        "description":
        "El comando solo se puede ejecutar en los servidores proporcionados.",
        "example": [
            "$nomention\n$onlyForServers[1077968892535775262;❌ ¡Este comando no se puede ejecutar en este servidor!]\n\n$c[Ponga su código aquí.]"
        ],
        "images_example": [
            f"{api}/funcion/images/onlyForServers.png"
        ],
        "deprecated":
        False
    },
    "onlyForUsers": {
        "name":
        "$onlyForUsers[]",
        "tag":
        "$onlyForUsers[Nombre de usuario;..;Mensaje de error]",
        "description":
        "El comando sólo puede ser ejecutado por usuarios con ciertos 'nombres de usuario'.",
        "example": [
            "$nomention\n$onlyForUsers[izana.py;❌ ¡Solo los usuarios con el nombre de usuario `izana.py` pueden ejecutar este comando!]\n\n$c[Ponga su código aquí.]"
        ],
        "images_example": [
            f"{api}/funcion/images/onlyForUsers.png"
        ],
        "deprecated":
        False
    },
    "onlyIf": {
        "name":
        "$onlyIf[]",
        "tag":
        "$onlyIf[Condicion]",
        "description":
        "Si el valor1 está relacionado en consecuencia (según el \"signo\") con el valor2, entonces el código se ejecuta. De lo contrario, se devuelve el mensaje de error proporcionado.",
        "example": [
            "$nomention\n$onlyIf[$message[1]==BDFD;❌ ¡El primer argumento de su mensaje debe ser \"BDFD\"!]\n¡Hola esto es $message[1]!"
        ],
        "images_example": [
            f"{api}/funcion/images/onlyIf.png"
        ],
        "deprecated":
        False
    },
    "onlyIfMessageContains": {
        "name":
        "$onlyIfMessageContains[]",
        "tag":
        "$onlyIfMessageContains[Mensajes;...;Mensaje de error]",
        "description":
        "Comprueba si el mensaje proporcionado contiene todas las palabras proporcionadas; de lo contrario, se devuelve el mensaje de error proporcionado.",
        "example": [
            "$nomention\n$onlyIfMessageContains[$message;Hola;Oye;❌ ¡Tu mensaje debe contener `Hola` y `Oye`!]\n\n$c[Ponga su código aquí.]"
        ],
        "images_example": [
            f"{api}/funcion/images/onlyMessageContains.png"
        ],
        "deprecated":
        False
    },


    "onlyNSFW": {
        "name":
        "$onlyNSFW[]",
        "tag":
        "$onlyNSFW[Mensaje de error]",
        "description":
        "Solo permite ejecutar el comando en canales NSFW.",
        "example": [
            "$nomention\n$onlyNSFW[Solo puedes usarlo en un canal NSFW]\n$c[Ponga su código aquí abajo.]"
        ],
        "images_example": [
            f"{api}/funcion/images/onlyNSFW.png"
        ],
        "deprecated":
        False
    },
    "onlyPerms": {
        "name":
        "$onlyPerms[]",
        "tag":
        "$onlyPerms[Permisos;...;Mensaje de error]",
        "description":
        "El comando solo se puede ejecutar si el usuario que lo ejecuta tiene todos los [permisos](https://nilpointer-software.github.io/bdfd-wiki/resources/permissions.html) proporcionados.",
        "example": [
            "$nomention\n$onlyPerms[kick;❌ ¡Necesitas el permiso `kick` para usar este comando!]\n$kickMention[$noMensajeMessage]"
        ],
        "images_example": [
            f"{api}/funcion/images/onlyPerms.png"
        ],
        "deprecated":
        False
    },

    "optOff": {
        "name": "$optOff[]",
        "tag": "$optOff[]",
        "description": "",
        "example": ["$c[Como podemos ver, los tres aleatorios arrojaron el mismo número. Arreglemos esto agregando $optOff]\n$optOff[El primer aleatorio: $random[1\;101]\nEl segundo aleatorio: $random[1\;101]\nEl tercer aleatorio: $random[1;101] \n]"],
        "images_example": [f"{api}/funcion/images/optOff.png"],
        "deprecated": False
    },


    "or": {
        "name": "$or[]",
        "tag": "$or[Condicion;...]",
        "description": "Devuelve \"true(verdadero)\" si al menos una de las condiciones proporcionadas es true(verdadera) `;` en caso contrario, devuelve \"false(falso)\".",
        "example": ["$nomention\n$if[$or[$message==hola;$message==HOLA;$message==Oye]==true]\nHola $username!\n$endif"],
        "images_example": [f"{api}/funcion/images/or.png"],
        "deprecated": False
    },


    "parentID": {
        "name": "$parentID[] $parentID",
        "tag": "$parentID[Canal ID]",
        "description": "Devuelve el ID de la categoría principal para el ID del canal dado y si en caso no se habre los corchetes devuelve el ID de la categoría principal del canal actual.",
        "example": ["$nomention\nCategoria ID: $parentID[$mentionedChannels[1]]"],
        "images_example": [f"{api}/funcion/images/parentID.png"],
        "deprecated": False
    },

    "ping": {
        "name": "$ping",
        "tag": "$ping",
        "description": "Devuelve el ping del nodo del bot, en milisegundos.",
        "example": ["Pong `$ping`ms"],
        "images_example": [f"{api}/funcion/images/ping.png"],
        "deprecated": False
    },

    "pinMessage": {
        "name": "$pinMessage[], $pinMessage",
        "tag": "$pinMessage[ID de canal; ID de mensaje]",
        "description": "Fija el mensaje de respuesta del bot en el canal actual pero si habre sus corchetes fija un mensaje específico usando su canal e ID de mensaje.",
        "example": ["$nomention\n$pinMessage[$channelID;$messageID]\nHe fijado tu mensaje!"],
        "images_example": [f"{api}/funcion/images/pingMessage.png"],
        "deprecated": False
    },

    "premiumExpireTime": {
        "name": "$premiumExpireTime[], $premiumExpireTime",
        "tag": "$premiumExpireTime[¿Tiempo Unix?]",
        "description": "Devuelve cuánto tiempo falta para que expire la premium si se habre sus corchetes se puede devolver en tiempo UNIX.",
        "example": ["$nomention\nMi premium vence en: $premiumExpireTime[true]"],
        "images_example": [f"{api}/funcion/images/premiumExpireTime.png"],
        "deprecated": False
    },

    "publishMessage": {
        "name": "$publishMessage[]",
        "tag": "$publishMessage[ID de canal;ID de mensaje]",
        "description": "Publica un mensaje desde un canal de anuncios a todos los servidores siguientes.",
        "example": ["$nomention\n$publishMessage[$mentionedChannels[1;false];$noMentionMessage]\n¡El mensaje ha sido publicado!"],
        "images_example": [f"{api}/funcion/images/publishMessage.png"],
        "deprecated": False
    },


    "random": {
        "name": "$random[], $random",
        "tag": "$random[mínimo; máximo]",
        "description": "Devuelve un número aleatorio entre 0 y 9 pero si se habre sus corchetes devuelve un número aleatorio entre \"mínimo\" y \"máximo\".",
        "example": ["$nomention\n🎲 ¡Obtuviste `$random[1;7]`!"],
        "images_example": [f"{api}/funcion/images/random.png"],
        "deprecated": False
    },


    "randomCategoryID": {
        "name": "$randomCategoryID[]",
        "tag": "$randomCategoryID[(ID de servidor)]",
        "description": "Devuelve una identificación de categoría aleatoria del servidor actual o del servidor proporcionado.",
        "example": ["$nomention\nCategoría aleatoria: $channelName[$randomCategoryID[]]"],
        "images_example": [f"{api}/funcion/images/randomCategoryID.png"],
        "deprecated": False
    },


    "randomChannelID": {
        "name": "$randomChannelID",
        "tag": "$randomChannelID",
        "description": "Devuelve una ID de canal aleatoria del servidor actual.",
        "example": ["$nomenntion\nAquí hay un canal aleatorio: <#$randomChannelID>"],
        "images_example": [f"{api}/funcion/images/randomChannelID.png"],
        "deprecated": False
    },


    "randomGuildID": {
        "name": "$randomGuildID",
        "tag": "$randomGuildID",
        "description": "Devuelve una ID de gremio aleatoria de los servidores en los que se encuentra el bot.",
        "example": ["$nomention\nServidor aleatorio: $serverName[$randomGuildID]"],
        "images_example": [f"{api}/funcion/images/randomGuildID.png"],
        "deprecated": False
    },
    "randomMention": {
        "name": "$randomMention",
        "tag": "$randomMention",
        "description": "Devuelve una mención aleatoria de un usuario del servidor actual.",
        "example": ["$nomention\nUsuario aleatorio: $randomMention"],
        "images_example": [f"{api}/funcion/images/randomMention.png"],
        "deprecated": False
    },




    "randomRoleID": {
        "name": "$randomRoleID[]",
        "tag": "$randomRoleID[Servidor ID]",
        "description": "Devuelve una identificación de función aleatoria del servidor actual o del servidor proporcionado.",
        "example": ["$nomention\nRol aleatorio: $roleName[$randomRoleID[]]"],
        "images_example": [f"{api}/funcion/images/randomRoleID.png"],
        "deprecated": False
    },


    "randomString": {
        "name": "$randomString[]",
        "tag": "$randomString[Longitud]",
        "description": "Genera una combinación aleatoria de letras/números.",
        "example": ["$nomention\nCadena: `$randomString[$message]`"],
        "images_example": [f"{api}/funcion/images/randomString.png"],
        "deprecated": False
    },
    "randomText": {
        "name": "$randomText[]",
        "tag": "$randomText[Texto;..]",
        "description": "Elige un valor de los valores proporcionados al azar.",
        "example": ["$nomention\n$randomText[Hola;Hol;Hey]!"],
        "images_example": [f"{api}/funcion/images/randomText.png"],
        "deprecated": False
    },



    "randomUser": {
        "name": "$randomUser",
        "tag": "$randomUser",
        "description": "Devuelve un nombre de usuario aleatorio del servidor actual.",
        "example": ["$nomention\nNombre de usuario aleatorio: $randomUser"],
        "images_example": [f"{api}/funcion/images/randomUser.png"],
        "deprecated": False
    },


    "randomUserID": {
        "name": "$randomUserID",
        "tag": "$randomUserID",
        "description": "Devuelve una ID de usuario aleatoria del servidor actual.",
        "example": ["$nomention\nID de usuario aleatorio: $randomUserID"],
        "images_example": [f"{api}/funcion/images/randomUserID.png"],
        "deprecated": False
    },



    "registerGuildCommands": {
        "name": "$registerGuildCommands[], $registerGuildCommands",
        "tag": "$registerGuildCommands[nombre del comando de barra diagonal;...]",
        "description": "Registra todos los comandos de barra diagonal del gremio actual pero si se habre sus corchetes los registros proporcionaron comandos de barra diagonal en el gremio actual.",
        "example": ["$nomention\n$registerGuildCommands[ayuda]\n¡Se registró con éxito el comando de barra diagonal del gremio `/help`!"],
        "images_example": [""],
        "deprecated": False
    },


    "removeComponents": {
        "name": "$removeAllComponents[], $removeAllComponents",
        "tag": "$removeComponents[Mensaje ID]",
        "description": "Elimina todos los componentes del mensaje actual pero si se habre sus corchetes elimina todos los componentes de un mensaje.",
        "example": ["$nomention\n$removeComponents[1201181797514485770]"],
        "images_example": [""],
        "deprecated": False
    },

    "removeButttons": {
        "name": "$removeButtons[], $removeButtons[]",
        "tag": "$removeButtons[Mensaje ID]",
        "description": "Remueves todos los botones pero si habre sus corchctes remueve todos los botones de un mensaje en especifico.",
        "example": ["$nomention\n$removeButton[$message[1]]\nSe eliminaron con éxito todos los botones del mensaje."],
        "images_Example": [],
        "deprecated": False
    },

    "removeComponent": {
        "name": "$removeComponent",
        "tag": "$removeComponent[$channelID;$messageID]",
        "description": "Elimina un determinado componente de un mensaje.",
        "example": ["$nomention\nSe eliminaron el componente del mensaje"],
        "images_example": [""],
        "deprecated": False
    },

    "removeContains": {
        "name": "$removeontains[]",
        "tag": "$removeontains[Palabra;...;Cantidad]",
        "description": "Elimina mensajes que contienen palabras proporcionadas. Elimina hasta la cantidad dada de mensajes más recientes.",
        "example": ["$nomention\n$onlyPerms[managemessages;❌ ¡Te falta el permiso `MANAGE_MESSAGES`!]\n$removeContains[https://discord.gg/;discord.gg/;https://discord.com/invite;$noMentionMessage]\n¡Mensajes `$noMentionMessage` eliminados exitosamente que contienen invitaciones!"],
        "images_example": [""],
        "deprecated": False
    },

    "removeEmoji": {
        "name": "$removeEmoji[]",
        "tag": "$removeEmoji[...]",
        "description": "Elimina el emoji dado del servidor.",
        "example": ["$nomention\n$removeEmoji[$message[1]]"],
        "images_example": [""],
        "deprecated": False
    },

    "removeLinks": {
        "name": "$removeLinks[], $removeLinks",
        "tag": "$removeLinks[Menssaje]",
        "description": "Elimina todos los enlaces de la respuesta del bot y si se habre sus corchetes elimina todos los enlaces del texto proporcionado.",
        "example": ["$nomention\n$removeLinks[$message[1]]"],
        "images_example": [""],
        "deprecated": False
    },

    "removeSplitTextElement": {
        "name": "$removeSplitTextElement[]",
        "tag": "$removeSplitTextElement[Indice]",
        "description": "Elimina un determinado elemento de los valores de `$textSplit[\]`.",
        "example": ["$nomention\n$textSplit[1-2-3;-]\n$removeSplitTextElement[2]\n$joinSplitText[-]"],
        "images_example": [f"{api}/funcion/images/removeSplitTextElement.png"],
        "deprecated": False
    },


    "repeatMessage": {
        "name": "$repeatMessage[]",
        "tag": "$repeatMessage[Cantidad;Mensaje]",
        "description": "Repite el texto proporcionado una cierta cantidad de veces.",
        "example": ["$nomention\n$repetMessage[5;Hola]"],
        "images_example": [f"{api}/funcion/images/repeatMessage.png"],
        "deprecated": False
    },
    "replaceText": {
        "name": "$replaceText[]",
        "tag": "$replaceText[Muestra;A Remplazar;Valor Nuevo;Cantidad]",
        "description": "Reemplaza 'Muestra' con 'A Remplazar' de 'Texto', puedes elegir cuántas 'Muestra' se reemplazan ingresando 'Cantidad'.",
        "example": ["$nomention\n$var[Muestra;¿Hola como estas?]\nResultado: $replaceText[$var[Muestra];como;donde;1]"],
        "images_example": [f"{api}/funcion/images/replaceText.png"],
        "deprecated": False
    },

    "repliedMessageID": {
        "name": "$repliedMessageID[], $repliedMessageID",
        "tag": "$repliedMessageID[Canall ID;Mensaje ID]",
        "description": "Devuelve el ID del mensaje respondido pero si se habre sus corchetes devuelve el ID del mensaje respondido del mensaje dado.",
        "example": ["$nomenntion\nEl ID del mensaje al que respondió es: $repliedMessageID[$channelID;$messageID]"],
        "images_example": [f"{api}/funcion/images/replaceText.png"],
        "deprecated": False
    },
    "reply": {
        "name": "$reply[], $reply",
        "tag": "$respuesta[ID de canal;ID de mensaje]$respuesta[ID de canal;ID de mensaje]",
        "description": "Respuestas al mensaje del autor. si se habre los corchetes responde a un mensaje proporcionado.",
        "example": ["$nomention\n$reply[$channelID;$messageID]\n¿Hola como estas?"],
        "images_example": [f"{api}/funcion/images/reply.png"],
        "deprecated": False
    },

    "replyIn": {
        "name": "$replyIn[]",
        "tag": "$replyIn[Tiempo]",
        "description": "El bot espera x _(cantidad de tiempo)_ antes de ejecutar el código.",
        "example": ["$nomention\n$replyIn[3s]\nHola $username!"],
        "images_example": [""],
        "deprecated": False
    },

    "resetChannelVar": {
        "name": "$resetChannelVar[]",
        "tag": "$resetChannelVar[Nombre de Variablede Variablede Variable]",
        "description": "Restablece una variable de canal a su valor predeterminado (el proporcionado en la aplicación) para cada canal en cada servidor.Restablece una variable de canal a su valor predeterminado (el proporcionado en la aplicación) para cada canal en cada servidor.",
        "example": ["$nomention\nSe restablecio la variable correctamente.\n$resetChannelVar[cookies]"],
        "images_example": [f"{api}/funcion/images/resetChannelVar.png"],
        "deprecated": False
    },

    "resetServerVar": {
        "name": "$resetServerVar[]",
        "tag": "$resetServerVar[Nombre de variable]",
        "description": "Restablece una variable de servidor a su valor predeterminado (el que se ingresa en la aplicación) para cada servidor.",
        "example": ["$nomention\nSe restablecio la variable de servidor correctamente.\n$resetServerVar[cookies]"],
        "images_example": [f"{api}/funcion/images/resetServerVar.png"],
        "deprecated": False
    },

    "resetUserVar": {
        "name": "$resetUserVar[]",
        "tag": "$resetUserVar[]",
        "description": "Restablece una variable de usuario a su valor predeterminado (el que se ingresa en la aplicación) para cada usuario, o solo para el usuario proporcionado.",
        "example": ["$nomention\nSe restablecio la variable de usuario globalmente para todos los de servidor correctamente.\n$resetUserVar[cookie]"],
        "images_example": [f"{api}/funcion/images/resetUserVar.png"],
        "deprecated": False
    },


    "roleCount": {
        "name": "$roleCount",
        "tag": "$roleCount",
        "description": "Devuelve cuántos roles hay en el servidor actual.",
        "example": ["$nomention\nHay roles $roleCount en $serverName[$guildID]"],
        "images_example": [f"{api}/funcion/images/roleCount.png"],
        "deprecated": False
    },


    "roleExists": {
        "name": "$roleExists",
        "tag": "$roleExists[ID rol]]",
        "description": "Devuelve si el ID proporcionado es o no un rol real.",
        "example": ["$nomention\n$rolExist[1239039039030939]\n$c[¡Este rol no existe!]"],
        "images_example": [f"{api}/funcion/images/roleExists.png"],
        "deprecated": False
    },
    "roleGrant": {
        "name": "$roleGrant[]",
        "tag": "$roleGrant[Usuario ID;-/+Rol ID]",
        "description": "Agrega o elimina roles del usuario proporcionado.",
        "example": ["$nomention\nSe agrego el rol de miembro correctamente a <@$mentioned[1;false]>\n$roleGrant[$mentioned[1;false];+1077972873613942905]"],
        "images_example": [f"{api}/funcion/images/roleGrant.png"],
        "deprecated": False
    },
    "roleID": {
        "name": "$roleID[]",
        "tag": "$roleID[Nombre del rol]",
        "description": "Devuelve el ID de un rol usando su nombre.",
        "example": ["$nomention\nID de rol para \"$message\": $roleID[$message]"],
        "images_example": [f"{api}/funcion/images/roleID.png"],
        "deprecated": False
    },
    "roleInfo": {
        "name": "$roleInfo[]",
        "tag": "$roleInfo[Mensaje]",
        "description": "Devuelve información sobre el rol mencionado. $roleInfo le permite crear un comando de información de rol sin utilizar un montón de funciones diferentes a la vez.",
        "example": ["$nomention\n$roleInfo[Nombre: {name}\nID: {roleID}\n¿Mencionable?: {mentionable}\nIzado: {hoist}\nColor: {color}\nPosicion: {position}]\n$title[Rol Informacion;1]"],
        "images_example": [f"{api}/funcion/images/roleInfo.png"],
        "deprecated": False
    },

    "roleName": {
        "name": "$roleName[]",
        "tag": "$roleName[Rol ID]",
        "description": "Devuelve el nombre de un rol usando su ID.",
        "example": ["$nomention\n$roleName[$highestRole[$authorID]]"],
        "images_example": [f"{api}/funcion/images/roleName.png"],
        "deprecated": False
    },

    "roleNames": {
        "name": "$roleNames",
        "tag": "$roleNames",
        "description": "Devuelve el nombre de cada función en el servidor actual.",
        "example": ["$nomention\n$description[Funciones del servidor: $roleNames]"],
        "images_example": [""],
        "deprecated": False
    },
    "rolePosition": {
        "name": "$rolePosition[]",
        "tag": "$rolePosition[Rol ID]",
        "description": "Devuelve la posición de un rol (siendo 1 el rol más alto).",
        "example": ["$nomention\nPosición de $description[<@&$findRole[$message]>: $rolePosition[$findRole[$message]]]"],
        "images_example": [""],
        "deprecated": False
    },

    "round": {
        "name": "$round[]",
        "tag": "$round[Número;(Decimal)]",
        "description": "Redondea el número proporcionado.",
        "example": ["$nomention\n$round[100.123;1]"],
        "images_example": [""],
        "deprecated": False
    },
    "scriptLanguage": {
        "name": "$scriptLanguage",
        "tag": "$scriptLanguage",
        "description": "Devuelve el nombre del lenguaje de secuencias de comandos utilizado por el comando.",
        "example": ["Este script usa el lenguaje: $scriptLangueage"],
        "images_example": [""],
        "deprecated": False
    },

    "second": {
        "name": "$second",
        "tag": "$second",
        "description": "Devuelve el segundo actual de este minuto.",
        "example": ["$nomention\nSegundo actual: $second"],
        "images_example": [""],
        "deprecated": False
    },
    "sendEmbedMessage": {
        "name": "$sendEmbedMessage",
        "tag": "$sendEmbedMessage[ID de canal;Contenido;(Título;URL del título;Descripción;Color;Autor;Icono de autor;Pie de página;Icono de pie de página;Miniatura;Imagen;¿Agregar marca de tiempo?;¿Devolver ID?)]",
        "description": "Envía un mensaje insertado al canal proporcionado. Los campos no necesarios se pueden dejar vacíos.",
        "example": ["$nomention\n$sendEmbedMessage[$channelID;;Título;https://discord.com/;description;000000;author;$authorAvatar;footer;$authorAvatar;$authorAvatar;$authorAvatar;false;false]"],
        "images_example": [""],
        "deprecated": False
    },
    "sendMessage": {
        "name": "$sendMessage[]",
        "tag": "$sendMessage[Mensaje;(¿Retornar ID?)]",
        "description": "Envía un nuevo mensaje al canal actual.",
        "example": [""],
        "images_example": [""],
        "deprecated": False
    },
    "serverChannelExists": {
        "name": "$serverChannelExists[]",
        "tag": "$serverChannelExists[Canal ID]",
        "description": "Comprueba si el canal existe en el servidor actual.",
        "example": ["$nomention\n$serverChannelExists[$message[1]]"],
        "images_example": [""],
        "deprecated": False
    },
}
