from graphene import ObjectType, String, Schema

class RootQuery(ObjectType):
    hello = String()

    def resolve_hello(self, info):
        return 'World'

schema = Schema(query=RootQuery)

if __name__ == "__main__":
    print('running')
    result = schema.execute('{ hello }')
    print(result.data['hello'])