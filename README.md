# p_srv
ChitChat microservice
```sh
docker run --rm -d -h cc_srv.local                                              \
           --name cc_srv                                             \
           -e "AMQP_URI=amqp://user:password@host"                  \
           -v /data/chitchat:/data                               \
           seliverstov/cc_srv:latest

```
