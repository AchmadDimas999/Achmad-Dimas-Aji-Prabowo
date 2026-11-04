"""Fungsi untuk mencetak dan menampilkan model."""


def print_models(unprinted_designs, completed_models):
    """Cetak setiap desain dan pindahkan ke daftar selesai."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Mencetak model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Tampilkan semua model yang sudah selesai dicetak."""
    print("Model yang sudah selesai:")
    for completed_model in completed_models:
        print(completed_model)