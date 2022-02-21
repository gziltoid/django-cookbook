$(document).ready(function () {
  $(".js-search-ingredients").select2({
    maximumSelectionLength: 10,
    placeholder: "Ингредиенты",
    allowClear: true,
  });
});
