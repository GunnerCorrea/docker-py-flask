# docker-py-flask
Project with Docker project. Running Python with Flask.

## Run docker container

To create image:

```docker build -t py-flask .```

To execute container:

```docker run -p 8080:80 -d py-flask```

## Edit host and port

Change **index.py** in root folder to change host and port.

```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
```