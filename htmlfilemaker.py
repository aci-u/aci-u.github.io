

username = str(input("Page name: "))



with open(f'{username}.html', 'a') as fi:
    message = f"""
    <!DOCTYPE html>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <html>
        <head>
            <meta charset="utf-8" />
            <link rel="stylesheet" href="styles.css" />
            <title>{username}</title>
        </head>
        
            <header>   
            </header>
        
            <body>        
            </body>
        
            <footer>         
            </footer>
    </html>"""
    fi.write(message)

with open(f'styles.css', 'a') as fi:
    fi.write("/* Start writing your CSS here!*/")