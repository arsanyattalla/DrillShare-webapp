const plugins = [
  [
    '@babel/plugin-transform-runtime',
    {
      absoluteRuntime: false,
      corejs: false,
      helpers: true,
      regenerator: true,
      version: '7.0.0-beta.0',
    },
    'babel-plugin-import',
    {
      libraryName: '@mui/material',
      libraryDirectory: '',
      camel2DashComponentName: false,
    },
    'core',
  ],
  [
    'babel-plugin-import',
    {
      libraryName: '@mui/icons-material',
      libraryDirectory: '',
      style: 'true',
      camel2DashComponentName: false,
    },
    'icons',
  ],
];

module.exports = {plugins};
