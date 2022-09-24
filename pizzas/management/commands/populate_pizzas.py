import random
import os
from django.core.management.base import BaseCommand
from pizzas.models import Pizza, Topping, PizzaSize
from media import pizza_images
from django_pizza import settings

# def get_images2():
#     path = settings.MEDIA_ROOT
#     img_list = os.listdir(path + '/pizza_images')
#     # context = {'images': img_list}
#     return img_list
def get_images(path):
    pizza_images = []
    for images in os.listdir(path):
        # print(os.listdir(path),"osdir")
        # print(path,"path")
        # print(images, "images")
        pizza_images.append(images)
    return pizza_images


def get_topping_value():
    topping_value = []
    for topping in Topping.objects.values_list():
        topping_value.append(topping[0])
    return topping_value


def random_picker(list_name):
    return random.choice(list_name)


# def random_topping():
#     # counter = random.randint(5,10)
#     topping_value = get_topping_value()
#     counter = 1
#     updated_list = []
#     for topping in get_topping_value():
#         print(topping, 'topping')
#         if topping not in updated_list:
#             updated_list.append(topping)
#             print(updated_list, 'list')
#             counter -= 1
#         if counter == 0:
#             break
#     return updated_list


# def random_pizza(names_list, sizes_list, images_list):
#         for pizza_name in names_list:
#             return Pizza.objects.get_or_create(name=pizza_name, toppings =generator(get_topping_value()),
#                                                sizes=generator(sizes_list), image=generator(images_list))


class Command(BaseCommand):
    help = 'Does shit'

    def handle(self, *args, **kwargs):
        toppings_path = open('pizzas/toppings.txt')
        names_path = open('pizzas/pizza_names.txt')
        images_path = os.path.normpath("media/pizza_images/")
        images_path = ("/Users/esterpavlov/PycharmProjects/django_pizza/media/pizza_images/")
        # uploaddir = Pizza.image.field.upload_to
        # another_try = get_images2()
        # images_path = MEDIA_ROOT
        toppings_list = [topping.strip() for topping in toppings_path]
        names_list = [name.strip() for name in names_path]
        sizes_list = PizzaSize.objects.values_list()
        # images2 = Pizza.objects.values_list("image")
        images_list = get_images(images_path)
        # image_test = [image.strip() for image in images_list]

        # images_list = get_images(uploaddir)
        for topping in toppings_list:
            Topping.objects.get_or_create(name=topping)
        toppings_dict = Topping.objects.values("id")
        # print(another_try)
        # print(images_path)
        # print(images_list)
        # for ids in topping_value:
            # print(ids)
        topping_ids = [id['id'] for id in toppings_dict]
        # print(topping_ids)
        # print(ids)
        # print(topping_value)
        # Pizza.objects.get_or_create(name=generator(names_list), toppings=generator(topping_ids), sizes=generator(sizes_list), image=generator(images_list))
        # print(images_list)

        # def save(self, *args, **kwargs):
        # obj = Pizza.objects.get(pk=1)
        # print(obj)
        # this_object = Pizza.objects.get(pk=self)
        # old_file_name = this_object.image.path
        #     # return old_file_name
        # print(old_file_name)
        # for image in Pizza.objects.values_list('image'):
            # print(image)

        # img_path = os.path.normpath("media/pizza_images")
        # print(img_path)
        # for image in os.listdir(img_path):
        #     return image
        # print(images_list)
        def pizza_generator(names_list, images_list):
        # def pizza_generator(names_list):
            counter = 5
            for name in names_list:
                Pizza.objects.get_or_create(name=name, price=0.2, image=random_picker(images_list))
                # Pizza.objects.get_or_create(name=name, price=0.2, image='pizza2.jpg')
                counter -=1
                if counter == 0:
                    break
            return "done"
        generate_pizza = pizza_generator(names_list, images_list)
        # print(generate_pizza)
        print(image_test)
        # print(Pizza.image._get_file)
        # print(Pizza.image.path())
        # print(Pizza.image.__dir__())
        # imagee = []
        # print(Pizza.image.__getattribute__('image'))
        # print(Pizza.image.url(imagee), 'imagee')
        # print(Pizza.image.url(Pizza.image), 'pizzaimg')
        # print(Pizza.image.url('image'), 'aoao')
        # print(os.path.normpath("media/pizza_images/"))
        # print(os.path.dirname("media/pizza_images/"))
        # print(os.path.abspath("media/pizza_images/"))
        # print(os.path.isfile("media/pizza_images/"))
        # print(os.path.realpath("media/pizza_images/"))
        # print(os.path.realpath("media/pizza_images/"))
        # print(os.path.lexists("media/pizza_images/"))
        # print(os.path.isabs("media/pizza_images/"))
        # imgg = []
        # for image in images_list:
        #     Pizza.objects.get_or_create(image=image)
        # print(len(Topping.name))
        # print(sum(Topping.objects.get_queryset()))
        # print(random_pizza(names_list, toppings_li
        # st, sizes_list, images_list))
        # print(random.choice(Topping.objects))
        # print(random_topic(toppings_list))
        # for topping_object in Topping.objects.only('name'):
        #     print(id(topping_object))

        def check(file):
            counter = 0
            for thing in file:
                print(thing,'this is the thing')
                counter +=1
                if counter == 31:
                    break
        # for topping in Topping.objects.values_list():
        #     test.append(topping)
        #     print(test)
        # random_pizza(names_list, sizes_list, images_list)
        # check(Topping.objects.values_list())
        # pizza_sizes = PizzaSize.size
        # for topping in toppings_list:
        #     Pizza.toppings.get_or_create(topping)
        # def check_direction(file):
        #     counter = 0
        #     for thing in file:
        #         print(thing)
        #         counter +=1
        #         if counter == 5:
        #             break
        # check_direction(toppings_list)
        # check_direction(pizza_names)
        # check_direction(Topping)