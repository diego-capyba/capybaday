# Script

## Preparação

- Resetar o banco
- Executar migrações
- Rodar seed de Locations e Riders
- Criar super usuário
- Rodar o servidor

## Trilha 1 - Querysets

- Apresentar o model
- Apresentar as URLs
- Apresentar a DragonIndexView
- Criar 10 dragões e testar
- Criar 1000 dragões e testar

### Count
- Mudar len() para count()

### Location
- Adicionar coluna location
- Testar novamente
- Mostrar o tempo da query na Django Debug Toolbar
- Adicionar a query no template
- Adicionar select_related()

### Riders
- Adicionar coluna riders
- Testar novamente
- Mostrar o tempo da query na Django Debug Toolbar
- Adicionar a query no template
- Adicionar prefetch_related()

## Trilha 2 - Model Serializers

### ModelSerializers básicos

- Criar a DragonViewSet
- Criar o Router e a URL
- Adicionar URL da browsable API
- Testar lista, detalhe e edição

### Mudança de serializer na view
- Criar DragonReadSerializer
- Alterar na view
- Testar edição

### Serializer híbrido
- Sobrescrever to_representation()
- Testar

## Trilha 3 - Serializer

- Explicar sobre a funcionalidade de batalha
- Adicionar power field em Dragon e Rider
- Criar action
- Interromper e criar serializers: DragonBattleSerializer e BattlePairSerializer
- Continuar action
- Interromper e criar método battle()
- Concluir action
- Testar
- Encerramento
