import graphene
import requests
from graphene import ObjectType


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
    company = graphene.Field(Company)
    # full_name = String()

    # def resolve_full_name(parent, info):
    #     return f"{parent.first_name} {parent.last_name}"


class Query(graphene.ObjectType):
    hello = graphene.String(description='A typical hello world')
    users = graphene.List(User)

    def resolve_hello(self, info):
        return 'World'

    def resolve_users(self, info):
        r = requests.get('https://jsonplaceholder.typicode.com/users')
        return r.json()


schema = graphene.Schema(query=Query)