const paths = {
  root: '/',
  items: '/items',
  getItemUrl(id) {
    return `/items/${id}`;
  },
};

const messageTypes = {
  warning: 'warning',
  primary: 'primary',
  danger: 'danger',
  success: 'success',
};

const foodTypes = {
  sweet: 'Sweet',
  sour: 'Sour',
  american: 'American',
  seafood: 'SeaFood',
  italian: 'Italian',
  french: 'French',
  chinese: 'Chinese',
  dessert: 'Dessert',
  thai: 'Thai',
};

export { paths, messageTypes, foodTypes };
