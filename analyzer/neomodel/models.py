from neomodel import (StructuredNode, StringProperty, BooleanProperty, DateProperty, RelationshipFrom, RelationshipTo)


class Group(StructuredNode):
    objectSid = StringProperty()
    distinguishedName = StringProperty(unique_index=True)
    description = StringProperty()
    whenCreated = DateProperty()
    securityDescriptor = StringProperty()
    genericAll = BooleanProperty()
    writeDacl = BooleanProperty()
    members = RelationshipFrom('User', 'MEMBER_OF')
    computers = RelationshipFrom('Computer', 'MEMBER_OF')


class User(StructuredNode):
    objectSid = StringProperty()
    distinguishedName = StringProperty(unique_index=True)
    servicePrincipalName = StringProperty()
    securityDescriptor = StringProperty()
    whenCreated = DateProperty()
    pwdLastSet = DateProperty()
    genericAll = BooleanProperty()
    writeDacl = BooleanProperty()
    group = RelationshipTo(Group, 'MEMBER_OF')


class Computer(StructuredNode):
    objectSid = StringProperty()
    distinguishedName = StringProperty(unique_index=True)
    operatingSystem = StringProperty()
    securityDescriptor = StringProperty()
    whenCreated = DateProperty()
    group = RelationshipTo(Group, 'MEMBER_OF')
