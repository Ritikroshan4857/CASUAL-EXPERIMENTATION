from app.core.assignment import assign_variant


def test_same_user_same_variant():
    v1 = assign_variant(101, "exp1", ["A", "B"])
    v2 = assign_variant(101, "exp1", ["A", "B"])

    assert v1 == v2


def test_different_users_distribution():
    variants = [assign_variant(i, "exp1", ["A", "B"]) for i in range(100)]

    assert "A" in variants
    assert "B" in variants


def test_experiment_salt_effect():
    results = set(
        assign_variant(101, f"exp{i}", ["A", "B"])
        for i in range(10)
    )

    # Across multiple experiments, we should see variation
    assert len(results) > 1