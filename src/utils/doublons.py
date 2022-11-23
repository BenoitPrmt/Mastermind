def tester_doublons(liste):
    """Permet de tester si tous les élements d'une liste sont identiques.

    Args:
        liste (list): Liste à tester

    Returns:
        bool: Retourne False si tous les élements sont identiques sinon True
    """

    element = None
    for ele in liste:
        if element is not None and ele != element:
            return True
        element = ele
    return False