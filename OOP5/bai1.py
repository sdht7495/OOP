class Hang_hoa:
    def __init__(self, ma_hang, ten_hang, nha_san_xuat, gia):
        self._ma_hang= ma_hang
        self._ten_hang= ten_hang
        self._nha_san_xuat= nha_san_xuat
        self._gia = gia

    def hien_thi(self):
        print(f"mã hàng: {self._ma_hang} | tên hàng:  {self._ten_hang} | nhà sản xuất:  {self._nha_san_xuat} | giá:  {self._gia} VND")
    
class hang_dien_may(Hang_hoa):
    def __init__(self, ma_hang, ten_hang, nha_san_xuat, gia, thoi_gian_bao_hanh, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_san_xuat, gia)
        self._thoi_gian_bao_hanh = thoi_gian_bao_hanh
        self._cong_suat = cong_suat

    def hien_thi(self):
        super().hien_thi()
        print(f"thời gian bảo hành: {self._thoi_gian_bao_hanh} tháng | công suất: {self._cong_suat}")


class hang_sanh_su(Hang_hoa):
    def __init__(self, ma_hang, ten_hang, nha_san_xuat, gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_san_xuat, gia)
        self._loai_nguyen_lieu = loai_nguyen_lieu

    def hien_thi(self):
        super().hien_thi()
        print(f"thời gian bảo hành: {self._thoi_gian_bao_hanh}")

class hang_thuc_pham(Hang_hoa):
    def __init__(self, ma_hang, ten_hang, nha_san_xuat, gia, ngay_san_xuat, ngay_het_han):
        super().__init__(ma_hang, ten_hang, nha_san_xuat, gia)
        self._ngay_san_xuat = ngay_san_xuat
        self._ngay_het_han = ngay_het_han

    def hien_thi(self):
        super().hien_thi()
        print(f"ngày sản xuất: {self._ngay_san_xuat} | ngày hết hạn: {self._ngay_het_han}")
