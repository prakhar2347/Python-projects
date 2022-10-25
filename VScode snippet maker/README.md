# VScode Snippet maker
Makes making VScode snippets easier. To make snippets of code in VScode below format is needed.
```json
"Snippet name": {
		"prefix": "prefix_to_call_snippet",
		"body": [
			// actual code content
		],
		"description": "description of the snippet"
	}
```

Here the `body` part is where our `snippet code` will go and there each line has to be in quotes `""` and after every line we require comma`,`.

Now we can do this manually as well but why do that 😛 ?
Just paste your code for which you want to make a snippet and run the py script.
and you will have the body part for the snippet ready 🎉