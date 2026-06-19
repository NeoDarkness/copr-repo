%global debug_package %{nil}

Name:           catppuccin-cursors
Version:        2.0.0
Release:        %autorelease
Summary:        Catppuccin cursor themes

License:        GPL-3.0-or-later
URL:            https://github.com/catppuccin/cursors

BuildArch:      noarch
BuildRequires:  unzip

Source0:        https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-frappe-blue-cursors.zip
Source1:        https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-frappe-dark-cursors.zip
Source2:        https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-frappe-flamingo-cursors.zip
Source3:        https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-frappe-green-cursors.zip
Source4:        https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-frappe-lavender-cursors.zip
Source5:        https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-frappe-light-cursors.zip
Source6:        https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-frappe-maroon-cursors.zip
Source7:        https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-frappe-mauve-cursors.zip
Source8:        https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-frappe-peach-cursors.zip
Source9:        https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-frappe-pink-cursors.zip
Source10:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-frappe-red-cursors.zip
Source11:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-frappe-rosewater-cursors.zip
Source12:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-frappe-sapphire-cursors.zip
Source13:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-frappe-sky-cursors.zip
Source14:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-frappe-teal-cursors.zip
Source15:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-frappe-yellow-cursors.zip

# lanjut sampai Source63 ...

%global flavors \
    frappe \
    latte \
    macchiato \
    mocha

%global accents \
    blue \
    dark \
    flamingo \
    green \
    lavender \
    light \
    maroon \
    mauve \
    peach \
    pink \
    red \
    rosewater \
    sapphire \
    sky \
    teal \
    yellow

Requires:       %{name}-frappe = %{version}-%{release}
Requires:       %{name}-latte = %{version}-%{release}
Requires:       %{name}-macchiato = %{version}-%{release}
Requires:       %{name}-mocha = %{version}-%{release}

%description
Meta package for all Catppuccin cursor themes.

%package frappe
Summary:        Catppuccin Frappé cursor themes

%description frappe
Catppuccin Frappé cursor themes in all accent colors.

%package latte
Summary:        Catppuccin Latte cursor themes

%description latte
Catppuccin Latte cursor themes in all accent colors.

%package macchiato
Summary:        Catppuccin Macchiato cursor themes

%description macchiato
Catppuccin Macchiato cursor themes in all accent colors.

%package mocha
Summary:        Catppuccin Mocha cursor themes

%description mocha
Catppuccin Mocha cursor themes in all accent colors.

%prep
%setup -q -T -c

sources=(
catppuccin-frappe-blue-cursors
catppuccin-frappe-dark-cursors
catppuccin-frappe-flamingo-cursors
catppuccin-frappe-green-cursors
catppuccin-frappe-lavender-cursors
catppuccin-frappe-light-cursors
catppuccin-frappe-maroon-cursors
catppuccin-frappe-mauve-cursors
catppuccin-frappe-peach-cursors
catppuccin-frappe-pink-cursors
catppuccin-frappe-red-cursors
catppuccin-frappe-rosewater-cursors
catppuccin-frappe-sapphire-cursors
catppuccin-frappe-sky-cursors
catppuccin-frappe-teal-cursors
catppuccin-frappe-yellow-cursors
)

i=0
for dir in "${sources[@]}"; do
    unzip -q "%{SOURCE${i}}" -d "${dir}"
    ((i+=1))
done

%install
install -d %{buildroot}%{_datadir}/icons

for dir in catppuccin-*-cursors; do
    install -d %{buildroot}%{_datadir}/icons/${dir}

    cp -a "${dir}"/* \
        %{buildroot}%{_datadir}/icons/${dir}/

    rm -f %{buildroot}%{_datadir}/icons/${dir}/LICENSE
    rm -f %{buildroot}%{_datadir}/icons/${dir}/AUTHORS
done

%files

%files frappe
%license catppuccin-frappe-blue-cursors/LICENSE
%doc catppuccin-frappe-blue-cursors/AUTHORS
%{_datadir}/icons/catppuccin-frappe-*-cursors/

%files latte
%license catppuccin-latte-blue-cursors/LICENSE
%doc catppuccin-latte-blue-cursors/AUTHORS
%{_datadir}/icons/catppuccin-latte-*-cursors/

%files macchiato
%license catppuccin-macchiato-blue-cursors/LICENSE
%doc catppuccin-macchiato-blue-cursors/AUTHORS
%{_datadir}/icons/catppuccin-macchiato-*-cursors/

%files mocha
%license catppuccin-mocha-blue-cursors/LICENSE
%doc catppuccin-mocha-blue-cursors/AUTHORS
%{_datadir}/icons/catppuccin-mocha-*-cursors/

%changelog
%autochangelog
