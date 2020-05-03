#!/usr/bin/env python3

from swagger_server import app


def main():
    app.create_app().run(port=8080, use_debugger=False)


if __name__ == "__main__":
    main()
