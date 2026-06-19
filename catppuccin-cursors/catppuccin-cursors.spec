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

Source16:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-latte-blue-cursors.zip
Source17:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-latte-dark-cursors.zip
Source18:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-latte-flamingo-cursors.zip
Source19:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-latte-green-cursors.zip
Source20:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-latte-lavender-cursors.zip
Source21:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-latte-light-cursors.zip
Source22:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-latte-maroon-cursors.zip
Source23:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-latte-mauve-cursors.zip
Source24:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-latte-peach-cursors.zip
Source25:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-latte-pink-cursors.zip
Source26:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-latte-red-cursors.zip
Source27:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-latte-rosewater-cursors.zip
Source28:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-latte-sapphire-cursors.zip
Source29:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-latte-sky-cursors.zip
Source30:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-latte-teal-cursors.zip
Source31:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-latte-yellow-cursors.zip

Source32:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-macchiato-blue-cursors.zip
Source33:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-macchiato-dark-cursors.zip
Source34:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-macchiato-flamingo-cursors.zip
Source35:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-macchiato-green-cursors.zip
Source36:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-macchiato-lavender-cursors.zip
Source37:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-macchiato-light-cursors.zip
Source38:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-macchiato-maroon-cursors.zip
Source39:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-macchiato-mauve-cursors.zip
Source40:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-macchiato-peach-cursors.zip
Source41:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-macchiato-pink-cursors.zip
Source42:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-macchiato-red-cursors.zip
Source43:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-macchiato-rosewater-cursors.zip
Source44:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-macchiato-sapphire-cursors.zip
Source45:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-macchiato-sky-cursors.zip
Source46:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-macchiato-teal-cursors.zip
Source47:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-macchiato-yellow-cursors.zip

Source48:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-mocha-blue-cursors.zip
Source49:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-mocha-dark-cursors.zip
Source50:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-mocha-flamingo-cursors.zip
Source51:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-mocha-green-cursors.zip
Source52:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-mocha-lavender-cursors.zip
Source53:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-mocha-light-cursors.zip
Source54:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-mocha-maroon-cursors.zip
Source55:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-mocha-mauve-cursors.zip
Source56:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-mocha-peach-cursors.zip
Source57:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-mocha-pink-cursors.zip
Source58:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-mocha-red-cursors.zip
Source59:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-mocha-rosewater-cursors.zip
Source60:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-mocha-sapphire-cursors.zip
Source61:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-mocha-sky-cursors.zip
Source62:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-mocha-teal-cursors.zip
Source63:       https://github.com/catppuccin/cursors/releases/download/v%{version}/catppuccin-mocha-yellow-cursors.zip

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

for archive in %{SOURCES}; do
    dir="$(basename "${archive}" .zip)"
    unzip -q "${archive}" -d "${dir}"
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
