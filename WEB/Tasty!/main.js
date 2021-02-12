import Express from "express";

const app = Express();

const page = `
<html>
    <head>
        <title>Tasty</title>
    </head>
    <body>
        <h1>Check out the delicious baked items available on this site!</h1>
    </body>
</html>
`

app.get('/', (req, res) => {
    res.cookie('Flag', 'd2FubmFoYWNre2MwMGsxM3NfNHIzX3Q0c3R5fQ==');
    res.write(page);
    res.end();
});

app.listen(1729);
