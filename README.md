similar to how JS functions by associating objects with TYPES that graphene provides > seems like these types allow the GraphQL engine to treat these objects as required (i.e. ObjectType, Schema, String, Int) > then create a python class and variables and have resolve_variable methods to tell the engine what to return for those queries > schema.execute(query) to test it out