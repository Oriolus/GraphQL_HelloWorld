import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType, utils
from data.model import Department as DepartmentModel, Kkt as KktModel, Azs as AzsModel


class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        # interfaces = (relay.Node, )


class DepartmentConnection(relay.Connection):
    class Meta:
        node = Department


class Azs(SQLAlchemyObjectType):
    class Meta:
        model = AzsModel
        # interfaces = (relay.Node, )

    def resolve_department(self, info, **kwargs):
        query = Department.get_query(info)
        return query


class AzsConnection(relay.Connection):
    class Meta:
        node = Azs


SortEnumAzs = utils.sort_enum_for_model(
    AzsModel,
    'SortEnumAzs',
    lambda c, d:
        c.upper() + ('_ASC' if d else '_DESC')
)


class Kkt(SQLAlchemyObjectType):
    class Meta:
        model = KktModel
        # interfaces = (relay.Node, )


class KktConnection(relay.Connection):
    class Meta:
        node = Kkt


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    kkt = SQLAlchemyConnectionField(KktConnection)
    department = SQLAlchemyConnectionField(DepartmentConnection)
    azs = SQLAlchemyConnectionField(
        AzsConnection,
        sort=graphene.Argument(
            SortEnumAzs,
            default_value=utils.EnumValue('id_asc', AzsModel.id.asc())
        ),
        id=graphene.Int(),
        offset=graphene.Int(),
        limit=graphene.Int()
    )

    def resolve_azs(self, info, sort, **kwargs):
        query = Azs.get_query(info)
        id = kwargs.get('id')
        offset = kwargs.get('offset', 0)
        limit = kwargs.get('limit', 10)
        if id:
            query = query.filter(AzsModel.id == id)
        # have no idea how correctly sort working, so...
        # if sort:
        #     if 'id_asc' in sort:
        #         query = query.order_by(AzsModel.id.asc())
        return query.order_by(AzsModel.id.asc()).offset(offset).limit(limit)


sale_point_schema = graphene.Schema(
    query=Query,
    types=[Department, Kkt, Azs]
)

