# client

## Project setup
```
npm install
```

### If the following error shows:
```Expected linebreaks to be 'LF' but found 'CRLF'  linebreak-style```
##### You can run the following to solve it
```
git config core.autocrlf false

git rm --cached -r .

git reset --hard
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
