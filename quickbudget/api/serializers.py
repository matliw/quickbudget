from rest_framework import serializers

from quickbudget import models
from quickbudget.models import Budget, Expense, Category, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]

    def create(self, validated_data):
        user = models.User.objects.create_user(
            username=validated_data["username"], password=validated_data["password"]
        )

        return user


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            "id",
            "name",
            "total",
            "description",
            "category",
            "created_timestamp",
            "budget_id",
        ]
        read_only_fields = ("id", "created_timestamp", "budget_id")

    def create(self, validated_data, **kwargs):
        validated_data["budget_id_id"] = self.context["request"].parser_context[
            "kwargs"
        ]["budget_id"]
        return super(ExpenseSerializer, self).create(validated_data)


class BudgetSerializer(serializers.ModelSerializer):
    expenses = ExpenseSerializer(many=True, read_only=True)
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Budget
        fields = [
            "id",
            "name",
            "budget_limit",
            "description",
            "created_timestamp",
            "expenses",
            "members",
            "creator"
        ]


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class \
        MemberAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ["members"]

    def update(self, instance, validated_data):
        for member in validated_data["members"]:
            instance.members.add(member)
            instance.save()

        return instance


class RemoveBudgetMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ["members"]

    def update(self, instance, validated_data):
        for member in validated_data["members"]:
            instance.members.remove(member)
            instance.save()

        return instance
