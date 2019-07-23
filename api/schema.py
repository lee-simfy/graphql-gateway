import aiohttp
import graphene
import requests
from graphene import ObjectType


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


class Geo(ObjectType):
    lat = graphene.Decimal()
    long = graphene.Decimal()


class Address(ObjectType):
    street = graphene.String()
    suite = graphene.String()
    city = graphene.String()
    zipcode = graphene.String()
    geo = graphene.Field(Geo)


class Company(ObjectType):
    name = graphene.String()
    catch_phrase = graphene.String()
    bs = graphene.String()


class User(ObjectType):
    id = graphene.String()
    name = graphene.String()
    username = graphene.String()
    email = graphene.String()
    address = graphene.Field(Address)
    phone = graphene.String()
    website = graphene.String()
    random = graphene.String()
    company = graphene.Field(Company)
    company1 = graphene.Field(Company)

    def resolve_random(self, info):
        return 'random'

    async def resolve_company1(self, info):
        async with aiohttp.ClientSession() as session:
            data = await fetch(session, 'https://jsonplaceholder.typicode.com/users')
            data = await fetch(session, 'https://jsonplaceholder.typicode.com/users')
            data = await fetch(session, 'https://jsonplaceholder.typicode.com/users')
            data = await fetch(session, 'https://jsonplaceholder.typicode.com/users')
            data = await fetch(session, 'https://jsonplaceholder.typicode.com/users')
        # data = requests.get('https://jsonplaceholder.typicode.com/users').json()
        # data = requests.get('https://jsonplaceholder.typicode.com/users').json()
        # data = requests.get('https://jsonplaceholder.typicode.com/users').json()
        # data = requests.get('https://jsonplaceholder.typicode.com/users').json()
        # data = requests.get('https://jsonplaceholder.typicode.com/users').json()
        return data[0]


class Query(graphene.ObjectType):
    hello = graphene.String(description='A typical hello world')
    users = graphene.List(User)

    def resolve_hello(self, info):
        return 'World'

    def resolve_users(self, info):
        r = requests.get('https://jsonplaceholder.typicode.com/users')
        return r.json()


schema = graphene.Schema(query=Query)