1. Створення image
'''docker build . -t tarassabat/homework-mod4web'''
2. Завантаження image в docker hub
'''docker push tarassabat/homework-mod4web'''
3. Скачування image з docker hub на linux server 
'''docker pull tarassabat/homework-mod4web'''
4. Запускаємо docker контейнер на сервері 
'''docker run —name homework-mod4web -p 3000:3000 -v'''
