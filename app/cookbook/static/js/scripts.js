$(document).ready(function () {
  $(".js-search-ingredients").select2({
    maximumSelectionLength: 8,
    placeholder: "Ингредиенты",
    allowClear: true,
  });
});
