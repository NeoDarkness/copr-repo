%global debug_package %{nil}

Name:           catppuccin-cursors
Version:        2.0.0
Release:        1%{?dist}
Summary:        Catppuccin cursor themes

License:        GPL-3.0-or-later
URL:            https://github.com/catppuccin/cursors

BuildArch:      noarch
BuildRequires:  unzip

Requires:       %{name}-frappe = %{version}-%{release}
Requires:       %{name}-latte = %{version}-%{release}
Requires:       %{name}-macchiato = %{version}-%{release}
Requires:       %{name}-mocha = %{version}-%{release}

%global release_url https://github.com/catppuccin/cursors/releases/download/v2.0.0

Source0:  %{release_url}/catppuccin-frappe-blue-cursors.zip
Source1:  %{release_url}/catppuccin-frappe-dark-cursors.zip
Source2:  %{release_url}/catppuccin-frappe-flamingo-cursors.zip
Source3:  %{release_url}/catppuccin-frappe-green-cursors.zip
Source4:  %{release_url}/catppuccin-frappe-lavender-cursors.zip
Source5:  %{release_url}/catppuccin-frappe-light-cursors.zip
Source6:  %{release_url}/catppuccin-frappe-maroon-cursors.zip
Source7:  %{release_url}/catppuccin-frappe-mauve-cursors.zip
Source8:  %{release_url}/catppuccin-frappe-peach-cursors.zip
Source9:  %{release_url}/catppuccin-frappe-pink-cursors.zip
Source10: %{release_url}/catppuccin-frappe-red-cursors.zip
Source11: %{release_url}/catppuccin-frappe-rosewater-cursors.zip
Source12: %{release_url}/catppuccin-frappe-sapphire-cursors.zip
Source13: %{release_url}/catppuccin-frappe-sky-cursors.zip
Source14: %{release_url}/catppuccin-frappe-teal-cursors.zip
Source15: %{release_url}/catppuccin-frappe-yellow-cursors.zip

Source16: %{release_url}/catppuccin-latte-blue-cursors.zip
Source17: %{release_url}/catppuccin-latte-dark-cursors.zip
Source18: %{release_url}/catppuccin-latte-flamingo-cursors.zip
Source19: %{release_url}/catppuccin-latte-green-cursors.zip
Source20: %{release_url}/catppuccin-latte-lavender-cursors.zip
Source21: %{release_url}/catppuccin-latte-light-cursors.zip
Source22: %{release_url}/catppuccin-latte-maroon-cursors.zip
Source23: %{release_url}/catppuccin-latte-mauve-cursors.zip
Source24: %{release_url}/catppuccin-latte-peach-cursors.zip
Source25: %{release_url}/catppuccin-latte-pink-cursors.zip
Source26: %{release_url}/catppuccin-latte-red-cursors.zip
Source27: %{release_url}/catppuccin-latte-rosewater-cursors.zip
Source28: %{release_url}/catppuccin-latte-sapphire-cursors.zip
Source29: %{release_url}/catppuccin-latte-sky-cursors.zip
Source30: %{release_url}/catppuccin-latte-teal-cursors.zip
Source31: %{release_url}/catppuccin-latte-yellow-cursors.zip

Source32: %{release_url}/catppuccin-macchiato-blue-cursors.zip
Source33: %{release_url}/catppuccin-macchiato-dark-cursors.zip
Source34: %{release_url}/catppuccin-macchiato-flamingo-cursors.zip
Source35: %{release_url}/catppuccin-macchiato-green-cursors.zip
Source36: %{release_url}/catppuccin-macchiato-lavender-cursors.zip
Source37: %{release_url}/catppuccin-macchiato-light-cursors.zip
Source38: %{release_url}/catppuccin-macchiato-maroon-cursors.zip
Source39: %{release_url}/catppuccin-macchiato-mauve-cursors.zip
Source40: %{release_url}/catppuccin-macchiato-peach-cursors.zip
Source41: %{release_url}/catppuccin-macchiato-pink-cursors.zip
Source42: %{release_url}/catppuccin-macchiato-red-cursors.zip
Source43: %{release_url}/catppuccin-macchiato-rosewater-cursors.zip
Source44: %{release_url}/catppuccin-macchiato-sapphire-cursors.zip
Source45: %{release_url}/catppuccin-macchiato-sky-cursors.zip
Source46: %{release_url}/catppuccin-macchiato-teal-cursors.zip
Source47: %{release_url}/catppuccin-macchiato-yellow-cursors.zip

Source48: %{release_url}/catppuccin-mocha-blue-cursors.zip
Source49: %{release_url}/catppuccin-mocha-dark-cursors.zip
Source50: %{release_url}/catppuccin-mocha-flamingo-cursors.zip
Source51: %{release_url}/catppuccin-mocha-green-cursors.zip
Source52: %{release_url}/catppuccin-mocha-lavender-cursors.zip
Source53: %{release_url}/catppuccin-mocha-light-cursors.zip
Source54: %{release_url}/catppuccin-mocha-maroon-cursors.zip
Source55: %{release_url}/catppuccin-mocha-mauve-cursors.zip
Source56: %{release_url}/catppuccin-mocha-peach-cursors.zip
Source57: %{release_url}/catppuccin-mocha-pink-cursors.zip
Source58: %{release_url}/catppuccin-mocha-red-cursors.zip
Source59: %{release_url}/catppuccin-mocha-rosewater-cursors.zip
Source60: %{release_url}/catppuccin-mocha-sapphire-cursors.zip
Source61: %{release_url}/catppuccin-mocha-sky-cursors.zip
Source62: %{release_url}/catppuccin-mocha-teal-cursors.zip
Source63: %{release_url}/catppuccin-mocha-yellow-cursors.zip

%description
Meta package for all Catppuccin cursor themes.

%package frappe
Summary:        Catppuccin Frappé cursor themes
%description frappe
Meta package for Catppuccin Frappé cursor themes.
%files frappe

%package latte
Summary:        Catppuccin Latte cursor themes
%description latte
Meta package for Catppuccin Latte cursor themes.
%files latte

%package macchiato
Summary:        Catppuccin Macchiato cursor themes
%description macchiato
Meta package for Catppuccin Macchiato cursor themes.
%files macchiato

%package mocha
Summary:        Catppuccin Mocha cursor themes
%description mocha
Meta package for Catppuccin Mocha cursor themes.
%files mocha

%define cursor_package(v:a:V:A:) \
%package -n catppuccin-%{v}-%{a}-cursors \
Summary:        Catppuccin %{V} %{A} cursor theme \
Requires:       catppuccin-%{v} = %{version}-%{release} \
%description -n catppuccin-%{v}-%{a}-cursors \
Catppuccin %{V} %{A} cursor theme. \
%files -n catppuccin-%{v}-%{a}-cursors \
%license %{_licensedir}/catppuccin-%{v}-%{a}-cursors \
%doc %{_docdir}/catppuccin-%{v}-%{a}-cursors \
%{_iconsdir}/catppuccin-%{v}-%{a}-cursors

%cursor_package -v frappe -a blue      -V Frappé -A Blue
%cursor_package -v frappe -a dark      -V Frappé -A Dark
%cursor_package -v frappe -a flamingo  -V Frappé -A Flamingo
%cursor_package -v frappe -a green     -V Frappé -A Green
%cursor_package -v frappe -a lavender  -V Frappé -A Lavender
%cursor_package -v frappe -a light     -V Frappé -A Light
%cursor_package -v frappe -a maroon    -V Frappé -A Maroon
%cursor_package -v frappe -a mauve     -V Frappé -A Mauve
%cursor_package -v frappe -a peach     -V Frappé -A Peach
%cursor_package -v frappe -a pink      -V Frappé -A Pink
%cursor_package -v frappe -a red       -V Frappé -A Red
%cursor_package -v frappe -a rosewater -V Frappé -A Rosewater
%cursor_package -v frappe -a sapphire  -V Frappé -A Sapphire
%cursor_package -v frappe -a sky       -V Frappé -A Sky
%cursor_package -v frappe -a teal      -V Frappé -A Teal
%cursor_package -v frappe -a yellow    -V Frappé -A Yellow

%cursor_package -v latte -a blue      -V Latte -A Blue
%cursor_package -v latte -a dark      -V Latte -A Dark
%cursor_package -v latte -a flamingo  -V Latte -A Flamingo
%cursor_package -v latte -a green     -V Latte -A Green
%cursor_package -v latte -a lavender  -V Latte -A Lavender
%cursor_package -v latte -a light     -V Latte -A Light
%cursor_package -v latte -a maroon    -V Latte -A Maroon
%cursor_package -v latte -a mauve     -V Latte -A Mauve
%cursor_package -v latte -a peach     -V Latte -A Peach
%cursor_package -v latte -a pink      -V Latte -A Pink
%cursor_package -v latte -a red       -V Latte -A Red
%cursor_package -v latte -a rosewater -V Latte -A Rosewater
%cursor_package -v latte -a sapphire  -V Latte -A Sapphire
%cursor_package -v latte -a sky       -V Latte -A Sky
%cursor_package -v latte -a teal      -V Latte -A Teal
%cursor_package -v latte -a yellow    -V Latte -A Yellow

%cursor_package -v macchiato -a blue      -V Macchiato -A Blue
%cursor_package -v macchiato -a dark      -V Macchiato -A Dark
%cursor_package -v macchiato -a flamingo  -V Macchiato -A Flamingo
%cursor_package -v macchiato -a green     -V Macchiato -A Green
%cursor_package -v macchiato -a lavender  -V Macchiato -A Lavender
%cursor_package -v macchiato -a light     -V Macchiato -A Light
%cursor_package -v macchiato -a maroon    -V Macchiato -A Maroon
%cursor_package -v macchiato -a mauve     -V Macchiato -A Mauve
%cursor_package -v macchiato -a peach     -V Macchiato -A Peach
%cursor_package -v macchiato -a pink      -V Macchiato -A Pink
%cursor_package -v macchiato -a red       -V Macchiato -A Red
%cursor_package -v macchiato -a rosewater -V Macchiato -A Rosewater
%cursor_package -v macchiato -a sapphire  -V Macchiato -A Sapphire
%cursor_package -v macchiato -a sky       -V Macchiato -A Sky
%cursor_package -v macchiato -a teal      -V Macchiato -A Teal
%cursor_package -v macchiato -a yellow    -V Macchiato -A Yellow

%cursor_package -v mocha -a blue      -V Mocha -A Blue
%cursor_package -v mocha -a dark      -V Mocha -A Dark
%cursor_package -v mocha -a flamingo  -V Mocha -A Flamingo
%cursor_package -v mocha -a green     -V Mocha -A Green
%cursor_package -v mocha -a lavender  -V Mocha -A Lavender
%cursor_package -v mocha -a light     -V Mocha -A Light
%cursor_package -v mocha -a maroon    -V Mocha -A Maroon
%cursor_package -v mocha -a mauve     -V Mocha -A Mauve
%cursor_package -v mocha -a peach     -V Mocha -A Peach
%cursor_package -v mocha -a pink      -V Mocha -A Pink
%cursor_package -v mocha -a red       -V Mocha -A Red
%cursor_package -v mocha -a rosewater -V Mocha -A Rosewater
%cursor_package -v mocha -a sapphire  -V Mocha -A Sapphire
%cursor_package -v mocha -a sky       -V Mocha -A Sky
%cursor_package -v mocha -a teal      -V Mocha -A Teal
%cursor_package -v mocha -a yellow    -V Mocha -A Yellow

%prep
%setup -c -T
for i in {0..63}; do
    eval zipfile=\%{SOURCE$i}
    [ -f "$zipfile" ] || continue
    unzip -q "$zipfile"
done

%install
install -dm755 %{buildroot}%{_iconsdir}

for i in {0..63}; do
    eval zipfile=\%{SOURCE$i}
    [ -f "$zipfile" ] || continue

    pkg=$(basename "$zipfile" .zip)

    install -dm755 %{buildroot}%{_iconsdir}/"${pkg}"
    cp -a "${pkg}"/* %{buildroot}%{_iconsdir}/"${pkg}"/

    install -dm755 %{buildroot}%{_licensedir}/"${pkg}"
    install -dm755 %{buildroot}%{_docdir}/"${pkg}"

    [ -f "${pkg}/LICENSE" ] && mv %{buildroot}%{_iconsdir}/"${pkg}"/LICENSE %{buildroot}%{_licensedir}/"${pkg}"/LICENSE
    [ -f "${pkg}/AUTHORS" ] && mv %{buildroot}%{_iconsdir}/"${pkg}"/AUTHORS %{buildroot}%{_docdir}/"${pkg}"/AUTHORS
done

%changelog
%autochangelog
