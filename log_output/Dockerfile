FROM python:3.10-alpine
WORKDIR /usr/src/app
COPY . .
# Chúng ta không cần CMD mặc định nữa vì sẽ định nghĩa trong Kubernetes
CMD ["python", "-u", "reader.py"]
