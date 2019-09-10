import graphene 

class RootQuery(graphene.ObjectType):
    hello = graphene.String()
    about = graphene.String()
    def resolve_hello(self, info):
        return 'World'
    def resolve_about(self, info):
        return 'About what'

schema = graphene.Schema(query=RootQuery)

if __name__ == "__main__":
    print('running')
    result = schema.execute('{ hello }')
    print(result.data['hello'])
    about_result = schema.execute('{ about }')
    print(about_result.data['about'])