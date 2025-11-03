def serialize_cliente(cliente):
    return {
        'id': cliente.id,
        'empresa': cliente.empresa,
        'setor': cliente.setor,
        'user': cliente.user
    }
