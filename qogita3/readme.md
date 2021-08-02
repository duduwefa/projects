Hello guys!

My API consists of an Address object and a User object.

<!-- class Address(models.Model):
        street_name = models.CharField(max_length=200)
        house_number = models.IntegerField()
        zip_code = models.CharField(max_length=200)
        user = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True)

        def __str__(self):
        return self.street_name + ' ' + str(self.house_number) + ' ' + self.zip_code

        #User will not be able to add a duplicated address to their account
        class Meta:
            unique_together = ('street_name','house_number','zip_code') -->

As you can see I declared an Address class which is inherited from Model class. 

In my models.py I decided to use the User class imported from authentication models.

I'm considering a OneToMany relationship between the two objects, thus one user can have multiple addresses.

<!-- user = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True) -->

As per one of the requirements the Meta class created makes sure user doesn't add duplicate addresses

<!-- class Meta:
            unique_together = ('street_name','house_number','zip_code') -->

I also created two serializers: UserSerializer and AddressSerializer in order to convert all the querysets and model instances to native Python datatypes that can then be easily rendered into JSON.

For my views.py file I created two views: the UserViewSet (inherits from GenericAPIView) provides only the 'read-only' actions, like list and retrieve. 

<!-- class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer -->

Unlike UserViewSet, the AddressViewSet (inherits from GenericAPIView) provides many actions like list, retrieve, create, update, delete.

<!-- class AddressViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AddressSerializer

    def get_queryset(self):
        queryset = Address.objects.filter(user=self.request.user)
        ad_id = self.request.query_params.get('ad_id')
        street_name = self.request.query_params.get('street_name')
        house_number = self.request.query_params.get('house_number')
        zip_code = self.request.query_params.get('zip_code')
        user_id = self.request.query_params.get('user_id')
        if street_name is not None:
            queryset = queryset.filter(street_name__startswith=street_name)
        if ad_id is not None:
            queryset = queryset.filter(id=ad_id)
        if house_number is not None:
            queryset = queryset.filter(house_number__startswith=house_number)
        if zip_code is not None:
            queryset = queryset.filter(zip_code__startswith=zip_code)
        if user_id is not None:
            queryset = queryset.filter(user=user_id)
        return queryset -->

You can see that I used BasicAuthentication authentication class and IsAuthenticated permission class as per one of the requirements (user is able to authenticate with username and password). 

I overwritten the retrieve method (get_queryset) to make sure that all the operations are permitted only in the objects (or addresses) associated with the user authenticated.

Below is my attempt to delete multiple addresses. I tried to use QueryDict. If I sent a DELETE /addresses?id=1&id=2&id=3, I thought I could iterate over the dict and delete objects using dict values. 

<!-- def destroy(self, request, *args, **kwargs):
        q = QueryDict(self.request.query_params.items())
        for ads_ids in q.values():
            instance = Address.objects.filter(id=ads_ids)
            instance.delete()
        #instance = self.get_object()
        #self.perform_destroy(instance)
        return Response(data='Delete successful',status=status.HTTP_204_NO_CONTENT) -->

I also didn't complete the logout bonus requirement. I did some research online and all of them said it is not possible to logout using basic authentication. But I found a tutorial using a third party app which had clear endpoints for logging out. The problem is it only works with TokenAuthentication, which actually would be a better choice for this code challenge as one of the assumptions says that the API would be used by public and internal websites and native mobile apps. However, I assume that I had to use BasicAuthentication due to the bonus requirement that says: "User is able to authenticate with username and a password".

