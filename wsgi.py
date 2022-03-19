from main import get_app, get_tracer
import os

service_name = os.environ["SERVICE_NAME"]
tracer = get_tracer(service_name, os.environ["JAEGER_HOST"])
app = get_app(tracer, service_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)